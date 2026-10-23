#!/usr/bin/env python3
"""Controle de coherence d'un paquet de documents, contre un registre des faits.

Usage :
    python controle.py <registre.yaml>            controle, ecrit le rapport, code 1 si anomalie
    python controle.py <registre.yaml> --figer    controle puis fige l'instantane valide
                                                  (+ --accepter-disparus si un fait a ete retire expres)
    python controle.py <registre.yaml> --texte    exporte le texte extrait (pour relecteur)

Trois couches :
1. Interdits : anciennes valeurs, formulations abandonnees, regles de style. Aucune
   occurrence toleree hors exception ("sauf", cherche dans la phrase de l'occurrence).
2. Faits : chaque valeur juste doit rester presente partout ou elle l'etait a
   l'instantane fige (et dans les documents listes en "doit_figurer").
3. Instantane : chaque paragraphe modifie depuis le dernier instantane fige est liste.
   Il est "prevu" s'il contient un fragment de corrections_prevues, sinon "a verifier".
"""
import difflib
import glob
import html
import json
import os
import re
import subprocess
import sys
import unicodedata
from html.parser import HTMLParser

import yaml

ESPACES = re.compile(r"[     \t ]+")
APOS = re.compile(r"[’‘ʼ]")
BLOCS = {
    "p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "td", "th",
    "section", "br", "text", "table", "ul", "ol", "header", "footer", "article",
    "figcaption", "caption", "dt", "dd", "blockquote", "title",
}
IGNORES = {"script", "style"}


def normaliser(texte):
    texte = unicodedata.normalize("NFC", texte)
    texte = APOS.sub("'", texte)
    texte = ESPACES.sub(" ", texte)
    return texte.strip()


class Extracteur(HTMLParser):
    """Texte d'une page HTML ou d'une slide, en blocs, notes <aside> a part."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocs, self.notes = [], []
        self.courant, self.pile_ignore, self.dans_aside = [], 0, 0

    def _couper(self):
        t = normaliser("".join(self.courant))
        if t:
            (self.notes if self.dans_aside else self.blocs).append(t)
        self.courant = []

    def handle_starttag(self, tag, attrs):
        if tag in IGNORES:
            self.pile_ignore += 1
        elif tag == "aside":
            self._couper()
            self.dans_aside += 1
        elif tag in BLOCS:
            self._couper()
        # le texte d'un aria-label (graphique) compte comme du texte lu
        for nom, valeur in attrs:
            if nom == "aria-label" and valeur:
                self._couper()
                (self.notes if self.dans_aside else self.blocs).append(normaliser(valeur))

    def handle_endtag(self, tag):
        if tag in IGNORES:
            self.pile_ignore = max(0, self.pile_ignore - 1)
        elif tag == "aside":
            self._couper()
            self.dans_aside = max(0, self.dans_aside - 1)
        elif tag in BLOCS:
            self._couper()

    def handle_data(self, data):
        if not self.pile_ignore:
            self.courant.append(data)

    def fin(self):
        self._couper()
        return self.blocs, self.notes


def lire(chemin):
    with open(chemin, encoding="utf-8-sig") as f:
        return f.read()


def unites_md(chemin):
    """Une unite par ligne non vide, numero de ligne garde."""
    unites = []
    for n, ligne in enumerate(lire(chemin).splitlines(), 1):
        t = normaliser(ligne)
        if t:
            unites.append((f"ligne {n}", t))
    return unites


def unites_html(chemin):
    ex = Extracteur()
    ex.feed(lire(chemin))
    blocs, notes = ex.fin()
    return [(f"bloc {i}", t) for i, t in enumerate(blocs, 1)] + [
        (f"notes {i}", t) for i, t in enumerate(notes, 1)
    ]


def unites_pdf(chemin):
    sortie = subprocess.run(
        ["pdftotext", "-enc", "UTF-8", chemin, "-"],
        capture_output=True, check=True,
    ).stdout.decode("utf-8", "replace")
    unites = []
    for page_n, page in enumerate(sortie.split("\f"), 1):
        for para in re.split(r"\n\s*\n", page):
            # recolle les mots coupes en fin de ligne, puis les lignes
            t = normaliser(re.sub(r"-\n(?=\w)", "", para).replace("\n", " "))
            if t:
                unites.append((f"page {page_n}", t))
    return unites


def unites_deck(dossier):
    index = os.path.join(dossier, "project", "deck.json")
    slides_dir = os.path.join(dossier, "project", "slides")
    if os.path.exists(index):
        ordre = json.loads(lire(index)).get("order", [])
    else:
        ordre = sorted(os.path.splitext(f)[0] for f in os.listdir(slides_dir))
    presents = {os.path.splitext(f)[0] for f in os.listdir(slides_dir) if f.endswith(".html")}
    ordre += sorted(presents - set(ordre))
    unites = []
    for sid in ordre:
        chemin = os.path.join(slides_dir, sid + ".html")
        if not os.path.exists(chemin):
            unites.append((f"slide {sid}", "[SLIDE ABSENTE DU DOSSIER]"))
            continue
        ex = Extracteur()
        ex.feed(lire(chemin))
        blocs, notes = ex.fin()
        unites += [(f"slide {sid} (visible)", t) for t in blocs]
        unites += [(f"slide {sid} (notes)", t) for t in notes]
    return unites


LECTEURS = {"md": unites_md, "txt": unites_md, "html": unites_html, "pdf": unites_pdf, "deck": unites_deck}


def type_de(chemin, declare):
    if declare:
        return declare
    if os.path.isdir(chemin):
        return "deck"
    return {".md": "md", ".txt": "txt", ".html": "html", ".htm": "html", ".pdf": "pdf"}.get(
        os.path.splitext(chemin)[1].lower(), "txt")


def charger_documents(registre, base):
    docs = {}
    for d in registre["documents"]:
        motif = os.path.join(base, d["chemin"])
        chemins = sorted(glob.glob(motif)) if any(c in d["chemin"] for c in "*?[") else [motif]
        if not chemins:
            docs[d["id"]] = {"erreur": f"aucun fichier pour {d['chemin']}", "unites": []}
            continue
        for chemin in chemins:
            did = d["id"] if len(chemins) == 1 else f"{d['id']}/{os.path.basename(chemin)}"
            if not os.path.exists(chemin):
                docs[did] = {"erreur": f"introuvable : {chemin}", "unites": []}
                continue
            try:
                unites = LECTEURS[type_de(chemin, d.get("type"))](chemin)
                docs[did] = {"chemin": chemin, "unites": unites}
            except Exception as e:  # un document illisible ne bloque pas les autres
                docs[did] = {"erreur": f"lecture impossible : {e}", "unites": []}
    return docs


def phrase_autour(texte, debut, fin):
    g = max(texte.rfind(c, 0, debut) for c in ".!?;")
    d_candidats = [i for i in (texte.find(c, fin) for c in ".!?;") if i != -1]
    d = min(d_candidats) if d_candidats else len(texte)
    return texte[g + 1: d + 1].strip()


def extrait(texte, debut, fin, marge=70):
    a, b = max(0, debut - marge), min(len(texte), fin + marge)
    return ("..." if a else "") + texte[a:b] + ("..." if b < len(texte) else "")


def compiler(motif):
    return re.compile(motif, re.MULTILINE)


def chercher_interdits(docs, interdits):
    trouves = []
    for it in interdits:
        rx, sauf = compiler(it["motif"]), compiler(it["sauf"]) if it.get("sauf") else None
        portee = it.get("documents")
        for did, doc in docs.items():
            if portee and not any(did == p or did.startswith(p + "/") for p in portee):
                continue
            for lieu, texte in doc["unites"]:
                for m in rx.finditer(texte):
                    if sauf and sauf.search(phrase_autour(texte, m.start(), m.end())):
                        continue
                    trouves.append({
                        "regle": it["nom"], "document": did, "lieu": lieu,
                        "extrait": extrait(texte, m.start(), m.end()),
                        "attendu": it.get("attendu", ""),
                    })
    return trouves


def presence_faits(docs, faits):
    carte = {}
    for f in faits:
        rx = compiler(f["valeur"])
        carte[f["id"]] = sorted(
            did for did, doc in docs.items() if any(rx.search(t) for _, t in doc["unites"]))
    return carte


def comparer_instantane(docs, instantane, prevues):
    changements = []
    for did, doc in docs.items():
        avant = instantane.get(did)
        apres = [t for _, t in doc["unites"]]
        lieux = [l for l, _ in doc["unites"]]
        if avant is None:
            changements.append({"document": did, "type": "nouveau document", "avant": "", "apres": "", "lieu": "", "prevu": False})
            continue
        sm = difflib.SequenceMatcher(a=avant, b=apres, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                continue
            a_txt, b_txt = " / ".join(avant[i1:i2]), " / ".join(apres[j1:j2])
            prevu = any(p in b_txt or p in a_txt for p in prevues)
            changements.append({
                "document": did, "type": {"replace": "modifie", "delete": "supprime", "insert": "ajoute"}[op],
                "lieu": lieux[j1] if j1 < len(lieux) else (lieux[-1] if lieux else ""),
                "avant": a_txt, "apres": b_txt, "prevu": prevu,
            })
    for did in instantane:
        if did not in docs:
            changements.append({"document": did, "type": "document disparu", "avant": "", "apres": "", "lieu": "", "prevu": False})
    return changements


def couper(t, n=300):
    return t if len(t) <= n else t[:n] + "..."


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    chemin_registre = os.path.abspath(args[0])
    base = os.path.dirname(chemin_registre)
    registre = yaml.safe_load(lire(chemin_registre))
    dossier_etat = os.path.join(base, registre.get("dossier_etat", "etat"))
    os.makedirs(dossier_etat, exist_ok=True)
    f_inst = os.path.join(dossier_etat, "instantane.json")
    f_carte = os.path.join(dossier_etat, "presence-des-faits.json")

    docs = charger_documents(registre, base)

    if "--texte" in args:
        sortie = os.path.join(dossier_etat, "texte-extrait.md")
        with open(sortie, "w", encoding="utf-8") as f:
            for did, doc in docs.items():
                f.write(f"\n\n# {did}\n\n")
                for lieu, t in doc["unites"]:
                    f.write(f"[{lieu}] {t}\n")
        print(f"Texte extrait : {sortie}")
        return

    interdits = list(registre.get("regles", [])) + [
        dict(it, nom=f"{f['id']} : {it.get('nom', 'ancienne valeur')}", attendu=it.get("attendu", f.get("sujet", "")))
        for f in registre.get("faits", []) for it in f.get("interdits", [])
    ]
    trouves = chercher_interdits(docs, interdits)
    carte = presence_faits(docs, registre.get("faits", []))

    disparus = []
    carte_figee = json.loads(lire(f_carte)) if os.path.exists(f_carte) else {}
    for f in registre.get("faits", []):
        attendus = set(carte_figee.get(f["id"], [])) | set(f.get("doit_figurer", []))
        for did in sorted(attendus - set(carte[f["id"]])):
            disparus.append({"fait": f["id"], "sujet": f.get("sujet", ""), "document": did})

    instantane = json.loads(lire(f_inst)) if os.path.exists(f_inst) else None
    changements = comparer_instantane(docs, instantane, registre.get("corrections_prevues", []) or []) if instantane else []

    erreurs = [(did, d["erreur"]) for did, d in docs.items() if d.get("erreur")]
    nb_unites = sum(len(d["unites"]) for d in docs.values())
    a_verifier = [c for c in changements if not c["prevu"]]

    lignes = [f"# Contrôle de cohérence : {registre.get('projet', '')}", ""]
    lignes.append(f"{len(docs)} documents lus, {nb_unites} paragraphes, {len(registre.get('faits', []))} faits, {len(interdits)} interdits.")
    lignes.append("")
    lignes.append(f"- Documents illisibles : **{len(erreurs)}**")
    lignes.append(f"- Interdits trouvés : **{len(trouves)}**")
    lignes.append(f"- Faits disparus d'un document : **{len(disparus)}**")
    if instantane is None:
        lignes.append("- Instantané : aucun encore figé (lancer avec --figer une fois le paquet validé)")
    else:
        lignes.append(f"- Changements depuis l'instantané : **{len(changements)}**, dont **{len(a_verifier)} non prévus** (régressions possibles)")
    lignes.append("")
    if erreurs:
        lignes += ["## Documents illisibles", ""] + [f"- {d} : {e}" for d, e in erreurs] + [""]
    if trouves:
        lignes += ["## Interdits trouvés", "", "| Règle | Document | Où | Extrait | Attendu |", "|---|---|---|---|---|"]
        for t in trouves:
            lignes.append(f"| {t['regle']} | {t['document']} | {t['lieu']} | {couper(t['extrait']).replace('|', '/')} | {t['attendu'].replace('|', '/')} |")
        lignes.append("")
    if disparus:
        lignes += ["## Faits disparus", "", "| Fait | Sujet | Document |", "|---|---|---|"]
        lignes += [f"| {d['fait']} | {d['sujet']} | {d['document']} |" for d in disparus] + [""]
    if changements:
        lignes += ["## Changements depuis l'instantané", "", "| Statut | Document | Où | Avant | Après |", "|---|---|---|---|---|"]
        for c in sorted(changements, key=lambda c: c["prevu"]):
            statut = "prévu" if c["prevu"] else "**à vérifier**"
            lignes.append(f"| {statut} | {c['document']} | {c['type']}, {c['lieu']} | {couper(c['avant']).replace('|', '/')} | {couper(c['apres']).replace('|', '/')} |")
        lignes.append("")
    lignes += ["## Présence des faits", "", "| Fait | Sujet | Documents où la valeur juste figure |", "|---|---|---|"]
    for f in registre.get("faits", []):
        lignes.append(f"| {f['id']} | {f.get('sujet', '')} | {len(carte[f['id']])} : {', '.join(carte[f['id']])} |")

    rapport = os.path.join(base, registre.get("rapport", "rapport-controle.md"))
    with open(rapport, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")

    if "--figer" in args:
        if trouves or erreurs:
            print("Refus de figer : il reste des interdits ou des documents illisibles.")
            sys.exit(1)
        if disparus and "--accepter-disparus" not in args:
            print("Refus de figer : des faits ont disparu. Corriger, ou relancer avec "
                  "--accepter-disparus si la disparition est voulue (décision changée).")
            sys.exit(1)
        with open(f_inst, "w", encoding="utf-8") as f:
            json.dump({did: [t for _, t in d["unites"]] for did, d in docs.items()}, f, ensure_ascii=False, indent=0)
        with open(f_carte, "w", encoding="utf-8") as f:
            json.dump(carte, f, ensure_ascii=False, indent=1)
        print("Instantané figé.")

    print(f"Rapport : {rapport}")
    print(f"illisibles={len(erreurs)} interdits={len(trouves)} faits_disparus={len(disparus)} "
          f"changements={len(changements)} non_prevus={len(a_verifier)}")
    sys.exit(1 if (erreurs or trouves or disparus or a_verifier) else 0)


if __name__ == "__main__":
    main()
