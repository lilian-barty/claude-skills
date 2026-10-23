#!/usr/bin/env python3
"""Auto-test de controle.py : un faux paquet de documents, chaque couche doit reagir.

Usage : python auto_test.py   (code 0 = tous les controles passent)
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
CONTROLE = os.path.join(ICI, "controle.py")

REGISTRE = r"""
projet: auto-test
documents:
  - {id: etude, chemin: etude.md}
  - {id: page, chemin: page.html}
  - {id: deck, chemin: deck, type: deck}
corrections_prevues: []
regles:
  - {nom: cadratin, motif: '[—–]'}
faits:
  - id: comite
    sujet: comite tous les 15 jours
    valeur: 'comité de pilotage tous les 15 jours'
    interdits:
      - {motif: 'comité de pilotage mensuel', nom: ancienne}
  - id: gamme
    sujet: gamme
    valeur: '1 jour, 2 jours et 5 jours'
    interdits:
      - motif: '1, 3 et 5 jours'
        sauf: "(?i)d'origine"
        nom: ancienne gamme
  - id: effectif
    sujet: effectif
    valeur: '1 200 salariés'
"""


def ecrire(base, chemin, texte):
    p = os.path.join(base, chemin)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(texte)


def lancer(base, *args):
    # Sans PYTHONIOENCODING, la console Windows (cp1252) écrit des octets que le parent ne sait pas décoder en UTF-8.
    r = subprocess.run([sys.executable, CONTROLE, "registre.yaml", *args], cwd=base,
                       capture_output=True, text=True, encoding="utf-8",
                       env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    rapport = open(os.path.join(base, "rapport-controle.md"), encoding="utf-8").read() \
        if os.path.exists(os.path.join(base, "rapport-controle.md")) else ""
    return r.returncode, r.stdout + r.stderr, rapport


def main():
    base = tempfile.mkdtemp(prefix="coherence-test-")
    resultats = []

    def verifier(nom, condition):
        resultats.append((nom, condition))

    try:
        ecrire(base, "registre.yaml", REGISTRE)
        ecrire(base, "etude.md", "# Etude\n\nUn comité de pilotage tous les 15 jours suit le projet.\n\n"
                                 "La gamme d'origine était 1, 3 et 5 jours.\n\nGamme : 1 jour, 2 jours et 5 jours.\n")
        # espace insecable dans le nombre : doit etre normalisee
        ecrire(base, "page.html", "<html><body><p>Effectif : 1&#160;200 salariés</p>"
                                  "<svg aria-label='Barres : 1 200 salariés'></svg></body></html>")
        ecrire(base, "deck/project/deck.json", json.dumps({"order": ["a"]}))
        ecrire(base, "deck/project/slides/a.html",
               "<section id='a'><h2>Effectif 1 200 salariés</h2><aside>Un comité de pilotage tous les 15 jours.</aside></section>")

        code, out, rap = lancer(base)
        verifier("paquet propre : code 0", code == 0)
        verifier("ancienne valeur citée volontairement (sauf) ignorée", "ancienne gamme" not in rap)
        verifier("espace insécable normalisée (effectif trouvé dans la page)", "| effectif | effectif | 2 : deck, page |" in rap)

        code, out, _ = lancer(base, "--figer")
        verifier("figer accepté sur un paquet propre", code == 0 and "figé" in out)

        # regression 1 : ancienne valeur reintroduite dans les notes du deck
        ecrire(base, "deck/project/slides/a.html",
               "<section id='a'><h2>Effectif 1 200 salariés</h2><aside>Un comité de pilotage mensuel.</aside></section>")
        code, out, rap = lancer(base)
        verifier("ancienne valeur trouvée dans les notes d'une slide", code == 1 and "slide a (notes)" in rap)
        verifier("valeur juste disparue du deck signalée", "| comite | comite tous les 15 jours | deck |" in rap)
        verifier("changement non prévu signalé", "**à vérifier**" in rap)
        code, out, _ = lancer(base, "--figer")
        verifier("figer refusé tant qu'il reste un interdit", code == 1 and "Refus" in out)

        # correction prevue : le changement passe en "prevu"
        ecrire(base, "deck/project/slides/a.html",
               "<section id='a'><h2>Effectif 1 200 salariés en France</h2><aside>Un comité de pilotage tous les 15 jours.</aside></section>")
        reg = REGISTRE.replace("corrections_prevues: []", "corrections_prevues: ['1 200 salariés en France']")
        ecrire(base, "registre.yaml", reg)
        code, out, rap = lancer(base)
        verifier("correction prévue reconnue comme prévue", code == 0 and "| prévu |" in rap and "**à vérifier**" not in rap)

        # regle de style
        ecrire(base, "etude.md", open(os.path.join(base, "etude.md"), encoding="utf-8").read() + "\nUn ajout — avec cadratin.\n")
        code, out, rap = lancer(base)
        verifier("tiret cadratin trouvé", code == 1 and "cadratin" in rap)

        # document manquant
        os.remove(os.path.join(base, "page.html"))
        code, out, rap = lancer(base)
        verifier("document manquant signalé comme illisible", code == 1 and "introuvable" in rap)
    finally:
        shutil.rmtree(base, ignore_errors=True)

    for nom, ok in resultats:
        print(("OK   " if ok else "ÉCHEC ") + nom)
    echecs = sum(1 for _, ok in resultats if not ok)
    print(f"{len(resultats) - echecs}/{len(resultats)} contrôles passés")
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
