# Mode 3 : cohérence d'un paquet de documents, sans régression

## Mode d'emploi (à afficher au lancement du mode)

> **Relecture, mode cohérence : des documents qui disent tous la même chose, et qui continuent à le dire**
> - Pour un paquet de documents liés (étude et annexes, fiches et leurs PDF, présentations et leurs notes, proposition et devis)
> - Je tiens un **registre des faits** : chaque chiffre et chaque décision, sa valeur juste, ses anciennes valeurs interdites
> - Un script passe tous les documents au crible après chaque modification ; un relecteur ne regarde ensuite que le sens
> - Une fois le paquet validé, je **fige un instantané** : à la passe suivante, tout changement que je n'avais pas prévu sort en "à vérifier"
> - Une décision change ? Je la change d'abord dans le registre, puis partout, puis je relance

## Quand ce mode s'impose

- Plusieurs documents qui partagent des chiffres ou des décisions.
- Toute correction qui touche plus de 3 documents liés, même s'ils partagent peu.
- Toute demande "contrôle de cohérence", "vérifie que tout est cohérent", "aucune régression".

Pour un document seul en plusieurs parties (une présentation, une étude), la section "Cohérence interne d'un document" du SKILL.md suffit.

## Pourquoi ce mode existe

Sur un paquet de 7 documents annoncés "tous cohérents", un contrôle par script a trouvé 108 écarts. Deux causes :
1. **Propagation incomplète** : une décision était corrigée dans l'étude mais pas dans une annexe, une note de présentation ou le PDF.
2. **Régression** : une correction en abîmait une autre (montants cassés par un script de remplacement, phrase tronquée en raccourcissant).

Une relecture à l'œil ne tient pas sur des milliers de paragraphes. Le contrôle se fait par script contre une source de vérité, et la relecture humaine ou par agent ne porte plus que sur le sens.

## Les trois couches

| Couche | Ce qu'elle attrape | Outil |
|---|---|---|
| 1. Registre des faits | une valeur ou une décision qui n'est pas la bonne | `registre.yaml` du projet |
| 2. Script de contrôle | anciennes valeurs encore présentes, valeur juste disparue d'un document, règles de style | `scripts/controle.py` |
| 3. Instantané | tout paragraphe modifié sans que ce soit prévu | `etat/instantane.json`, comparé à chaque passe |

## Prérequis

- Python 3 et le module PyYAML (`pip install pyyaml`).
- Pour lire les PDF : `pdftotext`, fourni par Poppler (sous Windows, par exemple avec `winget install oschwartz10612.Poppler`).

## Déroulé

### 1. Monter le dossier de contrôle (une fois par projet)

Dans le dossier du projet, un sous-dossier `controle/` contenant :
- `registre.yaml` : la liste des documents et des faits (modèle plus bas).
- pour une présentation en HTML, une copie locale au format lu par le script : `<dossier>/project/deck.json` (champ `order`, la liste des slides dans l'ordre) et `<dossier>/project/slides/<id>.html`. Les notes de l'orateur sont lues dans les balises `<aside>`. Si la présentation vit en ligne, rafraîchir cette copie avant chaque contrôle.

Pour remplir les faits : lire les notes et les décisions du projet, puis lister chaque chiffre clé, chaque décision tranchée et chaque formulation abandonnée. Un fait = un `sujet` (en clair), une `valeur` (expression régulière de la valeur juste), des `interdits` (expressions des anciennes valeurs, avec `sauf` pour les phrases où l'ancienne valeur est citée exprès, comme "la gamme d'origine était 1, 3 et 5 jours").

### 2. Contrôler

Depuis le dossier `controle/` :

```
python <dossier du skill>/scripts/controle.py registre.yaml
```

Le rapport `rapport-controle.md` liste les documents illisibles, les interdits trouvés (document, paragraphe, extrait), les faits disparus et, si un instantané existe, les changements depuis l'instantané. Code de sortie 0 : rien à signaler.

Trier chaque alerte. Une vraie erreur se corrige dans le document. Un faux positif se règle en resserrant le motif ou en ajoutant un `sauf` dans le registre, jamais en supprimant la règle. Relancer jusqu'à zéro.

### 3. Relecture de sens

`controle.py registre.yaml --texte` écrit `etat/texte-extrait.md` : tout le texte du paquet dans un seul fichier, paragraphe par paragraphe, avec son emplacement. Le confier à UN sous-agent relecteur neuf (sans le raisonnement de la session), avec le registre, pour chercher ce que le script ne voit pas : contradictions de sens, phrases abîmées, renvois cassés. Les corrections de texte suivent le SKILL.md (périmètre, ce que je ne touche pas, typographie). Une contradiction de sens sans version établie dans le registre ou les notes du projet ne se tranche pas : elle remonte à l'utilisateur, avec les options et ma recommandation. Corriger, relancer le script. Supprimer `texte-extrait.md` à la fin (il se régénère).

### 4. Figer

Quand le script est à zéro et la relecture traitée :

```
python <dossier du skill>/scripts/controle.py registre.yaml --figer
```

Le script refuse de figer s'il reste un interdit, un document illisible ou un fait disparu (`--accepter-disparus` si un fait a été retiré exprès, après décision).

### 5. À chaque modification suivante

1. Si une décision change : la changer d'abord dans le registre (nouvelle `valeur`, ancienne valeur passée dans `interdits`).
2. Écrire dans `corrections_prevues` un fragment de chaque nouveau texte voulu.
3. Modifier les documents, rafraîchir les copies des présentations, relancer le contrôle.
4. Tout changement non prévu sort en **à vérifier** : c'est une régression tant que le contraire n'est pas prouvé.
5. Zéro alerte : figer d'abord, puis vider `corrections_prevues`. Dans l'autre ordre, la passe qui fige affiche les changements comme "non prévus", même si l'instantané s'écrit bien.

En fin de réponse, une ligne : "contrôle de cohérence : X documents, 0 alerte, instantané figé".

## Modèle de registre

```yaml
projet: Nom du paquet
rapport: rapport-controle.md
dossier_etat: etat
documents:
  - {id: etude, chemin: ../ETUDE.md}
  - {id: annexes, chemin: ../annexes/*.md}           # un document par fichier
  - {id: fiche, chemin: ../fiche.html}
  - {id: fiche-pdf, chemin: "../fiche.pdf"}          # lu par pdftotext
  - {id: deck, chemin: decks/deck, type: deck}       # texte visible et notes séparés
corrections_prevues: []
regles:
  - {nom: Tiret cadratin, motif: '[—–]', attendu: virgule ou parenthèses}
faits:
  - id: comite
    sujet: Comité de pilotage tous les 15 jours
    valeur: 'tous les 15 jours'
    doit_figurer: [etude]            # facultatif, en plus de l'instantané
    interdits:
      - {motif: 'comité de pilotage mensuel', nom: ancienne fréquence}
      - motif: '1, 3 et 5 jours'
        sauf: "(?i)d'origine|abandonnée"   # cherché dans la phrase de l'occurrence
        documents: [etude, deck]           # facultatif : limite la portée
```

Les expressions régulières sont celles de Python. Le texte est normalisé avant contrôle : espaces insécables remplacées par des espaces, apostrophes courbes par des droites. Écrire donc `1 200` et `l'` simples. En YAML, entourer les motifs d'apostrophes simples (si le motif contient une apostrophe, de guillemets doubles).

## Pièges vérifiés

- **Dossier synchronisé** (Google Drive, OneDrive, Dropbox) : la synchronisation a déjà annulé des corrections. Après chaque écriture, attendre une quinzaine de secondes avant de relancer le contrôle ; le contrôle lui-même sert de vérification.
- **Scripts de correction en Python** : chaînes brutes `r"..."`. Un `\1` dans une chaîne normale a déjà détruit des montants ; le contrôle l'aurait signalé comme "changement non prévu".
- **Présentations** : le script lit la copie locale ; une copie périmée donne un faux "tout va bien". Toujours la rafraîchir avant de contrôler, et après chaque publication.
- **PDF** : un PDF non regénéré après la correction du HTML garde l'ancienne valeur ; le contrôle le voit parce que le PDF est un document du registre. Ne jamais l'en retirer.
- **Plusieurs correcteurs en parallèle** : un seul écrivain par fichier, et le contrôle se lance une fois que tous ont fini.
- **Chemins Windows dans un remplacement** : `sed` et les heredocs du shell avalent les antislashs (`fiches\sources` devient `fichessources`). Remplacer avec Python (chaînes brutes) et relire la ligne après écriture.
- **PDF d'une page HTML** : `msedge --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf=<sortie> <file:///...>`, puis `pdfinfo` (nombre de pages) et `pdftoppm -r 130 -png` pour regarder le rendu. Si la page déborde, baisser le `zoom` d'impression d'un centième à la fois.
- **Document ajouté au registre** : il sort toujours en "nouveau document, à vérifier" ; aucun fragment de `corrections_prevues` ne peut le marquer prévu. C'est attendu : le faire relire (relecture de sens), puis figer ; la passe suivante tombe à zéro.
- **Faux positifs** : un motif trop large attrape d'autres faits légitimes. L'ancrer sur le sujet (`comité[^.]{0,40}mensuel` plutôt que `mensuel`).

## Auto-test

`python scripts/auto_test.py` monte un faux paquet et vérifie que chaque couche réagit (11 contrôles : exception `sauf`, espaces insécables, notes de slide, fait disparu, changement non prévu, correction prévue, refus de figer, cadratin, document manquant). À relancer après toute modification de `controle.py`.

## Ce que le script ne fait pas

Il ne juge ni le sens, ni la mise en page, ni les graphiques. La relecture de sens (étape 3) et un contrôle visuel du rendu restent nécessaires.
