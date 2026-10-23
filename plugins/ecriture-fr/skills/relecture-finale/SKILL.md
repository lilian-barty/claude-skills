---
name: relecture-finale
description: "Relecture orthotypographique finale, en français comme en anglais : accords, conjugaison, coquilles, ponctuation, pronoms, prépositions, répétitions involontaires, typographie, cohérence interne. Texte collé, fichier (.docx, .md, .txt, .html, .pdf) ou document d'un tiers rendu en suivi des modifications. Inclut un mode cohérence pour un paquet de documents liés (étude et annexes, fiches et leurs PDF, présentations et leurs notes, proposition et devis) : registre des faits, script de contrôle, instantané contre les régressions, relecture de sens. Ne réécrit ni le style ni le rythme. Déclenche pour /relecture-finale, \"relis\", \"corrige les fautes\", \"proofread\", \"fix grammar\", \"relis ce fichier et enregistre la version corrigée\", \"contrôle de cohérence\", \"vérifie que tout est cohérent\", \"aucune régression\", ou toute correction qui touche plus de 3 documents liés. Pour rendre un texte plus fluide ou retirer les tics d'IA, c'est ecrire-sans-tics-ia."
---

# Relecture finale

## Mode d'emploi (à afficher au lancement)

> **/relecture-finale : les fautes partent, votre style reste**
> - Je corrige accords, conjugaison, coquilles, ponctuation et typographie
> - Je ne touche ni au rythme ni au vocabulaire : une phrase lourde mais juste est signalée, je ne la réécris pas
> - Texte collé : texte corrigé et journal. Fichier : copie `UPDATED_`. Document d'un tiers : suivi des modifications à valider
> - Plusieurs documents liés : mode cohérence (registre des faits, script, instantané)

## Ordre de priorité

Quand deux règles se contredisent, la plus haute l'emporte :

1. La demande explicite de l'utilisateur pour ce texte.
2. Le profil typographique choisi (section plus bas).
3. Le style de l'auteur : rythme, voix, vocabulaire.
4. Le périmètre de correction de ce skill.
5. Les conventions typographiques classiques, là où rien au-dessus ne tranche.

## Place dans la chaîne

Ce skill passe en dernier. Sur un texte produit avec une IA, `/ecrire-sans-tics-ia` (publié dans le même paquet) retire d'abord les tics ; la relecture finale vient ensuite. Un document écrit par quelqu'un d'autre (support de cours, document d'un client) ne passe que par ce skill : sa voix n'est pas celle de l'utilisateur.

## Ce que je corrige

C'est le seul périmètre, dans tous les modes :

- Accords, conjugaison, concordance des temps.
- Orthographe et coquilles. En anglais, je garde la variante d'origine (américaine ou britannique).
- Pronoms ambigus, articles, prépositions.
- Ponctuation fautive, selon le profil typographique.
- Répétitions involontaires. Une répétition voulue (anaphore, mot martelé) reste.
- Cohérence interne d'un document (section dédiée).
- Une phrase réellement incompréhensible : seul cas où je reformule, au plus près des mots de l'auteur, et je le note au journal.

## Ce que je ne touche pas

- **Le rythme.** Une phrase de 4 mots après une de 30, un fragment assumé, un paragraphe d'une ligne sont des choix. Je ne fusionne pas, je ne découpe pas, je n'ajoute aucune transition ("De plus", "Par ailleurs", "Toutefois").
- **La voix.** Vocabulaire inattendu mais juste, registre familier, intensité, tournures expressives : je garde. Je ne formalise pas et je ne remplace jamais un mot précis par un mot générique.
- **Le fond.** Aucune idée ajoutée, aucune nuance retirée, aucun allongement. Seule exception : une incohérence tranchée (section cohérence), toujours notée au journal.
- **La mise en forme.** Titres, gras, listes et liens restent en place.
- **Les tics d'IA.** Je n'ajoute ni formule d'ouverture ou de clôture, ni adjectif d'emphase (crucial, essentiel, robuste, incontournable).
- **La lisibilité au sens large.** Une phrase lourde, un enchaînement maladroit ou un ton inégal, mais grammaticalement juste : je le signale au journal, je ne le corrige pas.

En cas de doute entre une faute et un choix de style, je ne corrige pas : je signale.

Avant de garder une correction, une question : est-elle mesurablement meilleure, ou seulement différente ? Seulement différente, je l'annule.

## Typographie

### Toujours

- **Aucun tiret cadratin ni demi-cadratin** en ponctuation : virgule, point-virgule ou parenthèses. Le trait d'union et le tiret des intervalles ("2025-2026") restent.
- **Point médian** : retiré quand il sépare des phrases ou des arguments ; il reste quand il sépare des informations de même nature sur une ligne de métadonnées (signature, pied de page, mentions).
- **Une seule forme** de guillemets et d'apostrophe dans tout le texte.

### Profil typographique, à choisir

Par défaut, je suis la convention déjà en place dans le texte ; s'il n'en a pas, la typographie française classique. L'utilisateur peut demander le **profil clavier**, dans sa demande ou dans ses instructions permanentes (CLAUDE.md). Le profil choisi s'applique aussi à `/ecrire-sans-tics-ia`.

| Point | Typographie française classique (par défaut) | Profil clavier |
|---|---|---|
| Guillemets | Chevrons « ... », avec espaces insécables | Droits "..." ; je ne réintroduis jamais de chevrons |
| Apostrophe | Courbe ou droite, une seule forme | Droite ' |
| Nombres | Petits nombres en lettres dans un texte courant (le seuil varie selon les chartes), en chiffres devant une unité de mesure et pour les données | En chiffres dès 2, y compris en début de phrase et dans les titres : "dix jours" devient "10 jours". Restent en lettres "un", "une", les expressions figées ("en deux temps", "à quatre mains"), les noms propres et les citations |
| `%` et `€` | Espace insécable avant le signe ("75 %", "10 €") | Signe collé au chiffre ("75%", "10€") ; je retire les espaces existantes |
| Espaces avant `: ; ! ?` | Espace insécable en français | Inchangé |
| Virgules | Usage courant | Légères : je retire la virgule devant un complément court en fin de phrase, devant "parce que", et devant "et", "mais", "puis", "ou" qui relient deux morceaux courts. La virgule reste pour une vraie incise, une énumération et un complément placé en tête de phrase |

## Cohérence interne d'un document

Sur une présentation, une étude, un rapport ou tout document en plusieurs parties :

- Un nombre annoncé correspond aux éléments listés ("3 points" pour 3 points).
- Les totaux se recalculent.
- Un terme, un nom de rôle, une date ou un prix garde la même forme partout.
- Deux passages qui se contredisent : je corrige seulement si la bonne version est établie (registre des faits, décision la plus récente dans les notes du projet, document source). Sinon je ne tranche pas : la décision revient à l'utilisateur, à qui je pose la question avec les options et ma recommandation.

Chaque incohérence corrigée va au journal. Dès que plusieurs documents partagent des chiffres ou des décisions, ou qu'une correction touche plus de 3 documents liés, je passe au mode 3 : le contrôle se fait par script contre un registre des faits, plus à l'œil.

## Les trois modes

### Mode 1 : texte collé

1. Isoler le texte à relire. S'il n'y en a pas, demander en une ligne de le coller.
2. Repérer tout ce qui relève du périmètre de correction.
3. Pour chaque point, vérifier qu'il ne s'agit pas d'un choix de voix ou de rythme.
4. Corriger au plus petit changement possible.
5. Valider (section "Avant de rendre").

Rendu : le texte corrigé en entier, prêt à copier, puis le journal.

**Retouche ponctuelle** (une phrase, un titre, un paragraphe désigné) : je ne change que la zone demandée, plus le strict minimum autour pour que la phrase se lise (un pronom, une liaison). Je rends seulement les lignes modifiées, chacune avec son motif, et une variante si le choix est serré. Un problème grave vu ailleurs (affirmation fausse, lien cassé) se signale en une ligne, sans être corrigé.

### Mode 2 : fichier

Formats : .docx, .md, .txt, .html, .pdf textuel. Pour un autre format, je le dis en une ligne et je propose une conversion.

1. Lire le fichier en entier avant toute correction.
2. Appliquer les étapes 2 à 5 du mode 1.
3. Enregistrer, en conservant la mise en forme.

Particularités :
- **HTML** : je corrige le texte visible et les textes lus par les visiteurs ou les moteurs (`alt`, `title`, `meta description`), jamais le code.
- **PDF** : il ne se réécrit pas proprement. Je corrige la source (HTML, .docx) puis je regénère le PDF ; sans source, je livre la version corrigée en .docx ou .md.

Nommage, dans cet ordre :
1. Le nom indiqué par l'utilisateur.
2. Sinon, une copie `UPDATED_<nom d'origine>` à côté de l'original, qui reste intact. Exemple : `programme.docx` devient `UPDATED_programme.docx`.
3. Exception : un fichier suivi par git se corrige sur place, l'historique sert de version d'origine. Une copie `UPDATED_` y deviendrait un fichier mort.

### Document d'un tiers

Programme de cours, formulaire, support, document d'un client ou d'une école : je n'applique rien sans l'accord de l'utilisateur.

1. Je livre en une fois une version Word en suivi des modifications, chaque correction avec son motif en commentaire.
2. Je liste toutes les corrections, chacune à garder ou à refuser, avec ma recommandation.
3. Après la réponse, je livre la version propre avec les seules corrections validées.

Si l'utilisateur fournit d'autres documents du même dossier, je contrôle la cohérence avec eux (noms des rôles, dates, consignes) et je note chaque écart. Au-delà de 3 documents liés, mode 3.

### Mode 3 : cohérence d'un paquet de documents

Déclenché par "contrôle de cohérence", "vérifie que tout est cohérent", "aucune régression", ou dès que plusieurs documents partagent des chiffres ou des décisions (étude et annexes, fiches et leurs PDF, présentations et leurs notes, proposition et devis), ou qu'une correction touche plus de 3 documents liés. J'affiche d'abord le mode d'emploi du mode, puis je suis le déroulé de [coherence-paquet.md](references/coherence-paquet.md). Outils : `scripts/controle.py` (contrôle, `--figer`, `--texte`) et `scripts/auto_test.py`.

## Avant de rendre

- Compter : autant de lignes au journal que de corrections dans le texte. Si les nombres diffèrent, reprendre.
- Plus aucune faute du périmètre.
- Typographie vérifiée par recherche dans le texte : tirets cadratins et demi-cadratins, points médians, formes de guillemets et d'apostrophes mélangées, puis les points du profil choisi.
- Sens inchangé, sauf incohérence tranchée et notée.
- Rythme et vocabulaire de l'auteur intacts.

## Rendu

- **Journal des modifications**, toujours, sauf si l'utilisateur demande le fichier seul. Une ligne par correction : avant, après, motif. Puis une rubrique "Signalé, non corrigé" pour les doutes de style et les phrases lourdes. Jusqu'à 5 lignes, il va dans la réponse ; au-delà, dans un fichier `JOURNAL_<nom>.md` à côté du livrable.
- **Fichier** : nom et emplacement confirmés en une ligne.
- **Fin de réponse** : le nombre de corrections, ce qui reste à arbitrer et la seule action suivante. Pas de formule d'encouragement ni de politesse.

## Module EXHAUSTIVITÉ

- Traiter TOUTES les entrées : si N documents ou passages sont fournis, N sont traités. Interdit : "et ainsi de suite", "exemples représentatifs", "les principaux éléments".
- Avant de rendre, compter les entrées et les sorties ; si les nombres diffèrent, reprendre.
- Aucun champ à remplir, "TODO" ni section vide dans le livrable final.
- Ne jamais s'arrêter à mi-tâche pour proposer de continuer : rendre le résultat complet en une fois.
- Si la sortie complète ne tient pas en une fois, découper en lots et livrer TOUS les lots, jamais un échantillon présenté comme complet.

Les seules questions permises sont les arbitrages qui reviennent à l'utilisateur (incohérence sans version établie, corrections d'un document de tiers). Elles partent toutes en une fois, après le travail complet, jamais au compte-gouttes.

## Sorties sans tics de modèle

Tout ce que ce skill produit (texte corrigé, journal, liste de choix, consigne pour un relecteur) doit pouvoir passer pour le travail soigné d'une personne compétente : pas de remplissage, pas d'emphase qui ne mesure rien, pas de tiret cadratin, pas de fait ni de chiffre inventé. Avant de rendre, relire sa propre sortie contre ces interdits et corriger sans le commenter.
