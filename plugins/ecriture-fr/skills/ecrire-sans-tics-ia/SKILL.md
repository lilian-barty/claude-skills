---
name: ecrire-sans-tics-ia
description: "Écrire ou relire un texte, en français ou en anglais, pour qu'il ne porte plus les tics des textes générés par IA : formules creuses, emphase qui ne mesure rien, oppositions de décor, phrases toutes de la même longueur, mots attendus, typographie de machine. Détecte la langue et applique les règles françaises (lexique, 19 structures à éviter, typographie) ou anglaises (21 catégories, table de 43 remplacements, relecture en deux passes, recherche avant lecture sur les fichiers HTML). Deux usages : écrire du neuf, ou retirer les tics d'un texte existant sans toucher au fond. Déclenche pour /ecrire-sans-tics-ia, écrire ou relire un texte pour qu'il ne sonne pas IA, \"enlève les tics d'IA\", \"ça sonne ChatGPT\", ou en anglais : remove AI-isms, clean up AI writing, make this sound less like AI, audit an English text or an HTML page for AI writing patterns. Ne sert pas à tromper un détecteur ni à faire passer pour humain un texte qui ne l'est pas."
---

# Écrire sans tics d'IA, en français et en anglais

Ce skill aide à écrire avec l'IA des textes précis et rythmés, qui disent quelque chose. Il n'a pas été conçu pour cacher l'usage d'une IA ni pour tromper un outil de détection.

## Mode d'emploi (à afficher au lancement)

Toujours commencer par ce court mode d'emploi, adapté au contexte, avant de travailler :

> **/ecrire-sans-tics-ia : un texte qui ne sonne pas IA, en français ou en anglais**
> - `/ecrire-sans-tics-ia [consigne, texte ou chemin de fichier]`
> - J'écris du neuf, ou je retire les tics d'un texte existant sans toucher au fond ni aux faits
> - La langue est détectée sur le texte. Pour un fichier HTML, je cherche les tics par recherche avant de lire
> - Pour un score chiffré avant de reprendre un texte : `/diagnostic-tics-ia`. Ensuite, pour les fautes et la typographie : `/relecture-finale`

Si la consigne ou le texte est déjà fourni, enchaîner directement après le mode d'emploi.

## Choisir la langue

1. **Détecter la langue du texte à produire ou à relire**, pas celle de la conversation. Une consigne en français pour un public anglophone donne un texte anglais.
2. **Français** : appliquer tout ce fichier.
3. **Anglais** : lire `references/anglais.md` en entier et l'appliquer. Restent valables dans les deux langues : prévisibilité et régularité, mode relecteur (le sens et les faits ne bougent pas), garde-fou contre la surcorrection, aucun tiret cadratin, aucune opposition de décor (structure 14), module EXHAUSTIVITÉ.
4. **Texte mixte** (page bilingue, support anglais avec notes en français) : traiter chaque passage avec les règles de sa langue, et ne relire que les passages demandés.
5. **Fichier HTML ou structuré, quelle que soit la langue** : appliquer la méthode "recherche avant lecture" de `references/anglais.md` ; ne jamais relire un long fichier HTML d'une traite. Si le fichier contient de gros blocs (images en base64, scripts), extraire les textes par script.

Deux casquettes :
- **Auteur** : écrire du neuf, juste du premier coup.
- **Relecteur** : reprendre un texte existant (souvent produit par une IA) et en retirer les tics sans en changer le fond.

## Pourquoi un texte sonne machine

Deux propriétés trahissent un texte généré bien plus qu'une liste de mots.

**La prévisibilité.** Un modèle choisit presque toujours le mot le plus probable. Le texte coule, et chaque mot est celui qu'on attendait. Une personne qui écrit surprend : un mot précis à la place du générique, une image inattendue, une tournure qui n'était pas la plus économique. Remplacer un mot banni par son synonyme le plus courant ne change rien : la phrase reste aussi attendue. Il faut un choix moins probable, et juste.

**La régularité.** Un modèle produit des phrases de longueur égale, bien équilibrées. Une personne alterne une phrase de trente mots et une de quatre, un paragraphe long et une ligne sèche. Viser une vraie variation.

Le reste du skill sert ces deux leviers. Un texte peut ne contenir aucun mot de la liste et sonner machine de bout en bout s'il est trop attendu et trop régulier.

## Mode relecteur : reprendre un texte existant

Le fond appartient à l'auteur, on ne touche qu'à la forme.

1. **Repérer avant de réécrire.** Passer le texte au crible des sections suivantes (lexique, structures, typographie) et noter les passages trop attendus et le rythme trop égal. On sait quoi corriger avant de toucher une phrase.
2. **Préserver le sens et les faits.** Aucun chiffre, nom, argument ni nuance ne change. Si une correction de style modifie le propos, la refuser ou poser la question.
3. **Corriger par ordre de gravité.** D'abord ce qui se voit le plus : formules d'ouverture et de clôture, structures à éviter, tirets cadratins, rythme uniforme. Ensuite le lexique creux. En dernier le grain fin.
4. **Ne pas surcorriger.** Le texte relu doit rester reconnaissable par son auteur (voir le garde-fou plus bas). On retouche le minimum nécessaire.
5. **Rendre.** Le texte corrigé, puis, si l'auteur le demande, deux lignes sur les types de corrections faites.

## Registre plancher : le français écrit standard

Écrire vivant ne veut pas dire écrire oral : les écarts d'un bon auteur sont des choix.

Formes à éviter :
- `t'as`, `t'avais`, `t'es` : `tu as`, `tu avais`, `tu es`
- `on est pas`, `c'est pas` : garder la négation complète
- `faut` sans sujet : `il faut`
- `y'a` : `il y a`
- `va pas`, `marche pas` : `ne va pas`, `ne marche pas`

## Lexique creux

Cette liste illustre, elle n'épuise pas. Bannir le **procédé** en même temps que les mots : remplacer `crucial` par `déterminant`, `clé` ou `central` laisse le défaut entier.

Le procédé à éliminer est l'emphase qui ne mesure rien. "Un résultat déterminant" n'en dit pas plus que "un résultat qui a fait gagner trois points". Couper l'adjectif d'insistance ou le remplacer par un fait, y compris pour tout synonyme absent de la liste.

**Adjectifs creux** : crucial, fondamental, essentiel, capital, vital, robuste, holistique, nuancé, multifacette, incontournable, optimal, pertinent, innovant, révolutionnaire.

**Verbes creux** : exploiter (au sens de tirer parti), leverager, naviguer (au sens figuré), appréhender, façonner, catalyser, orchestrer, déployer (une stratégie), booster, sublimer, optimiser.

**Noms de jargon d'entreprise** : écosystème, paysage (concurrentiel, médiatique), paradigme, synergies, feuille de route, parties prenantes, valeur ajoutée, impact (non chiffré), trajectoire, dynamique, vecteur, levier.

**Formules d'ouverture** : "Dans le monde d'aujourd'hui...", "À l'ère du numérique...", "Il est indéniable que...", "Force est de constater que...", "Il convient de noter que...", "Dans le contexte actuel...".

**Formules de clôture** : "En conclusion, nous pouvons affirmer que...", "Pour résumer les points clés...", "N'hésitez pas à me contacter...", "Pour aller plus loin...", "L'avenir appartient à ceux qui...".

**Registre administratif** : "au sein de" devient "dans" ; "dans le cadre de" devient "pour" ou "lors de" ; "afin de" devient "pour" ; "permettre de" employé à tout propos se remplace par le verbe précis ; "en termes de" devient "sur" ou "concernant" ; "à même de" devient "capable de".

**Métaphores qui donnent vie à l'abstrait** : "vos données parlent", "le moteur de votre croissance", "la recette secrète", "la boussole", "le tableau de bord devient enfin honnête". Dire ce que la donnée montre ("les posts du mardi reçoivent plus de réponses"), où elle se trouve, ce qui fait venir les clients.

**Calques de l'anglais** : adresser un problème (traiter), impacter (affecter, toucher), réaliser que (se rendre compte que), opportunité (occasion), supporter au sens de soutenir (soutenir, prendre en charge), éventuellement au sens de finalement, délivrer (livrer, fournir), initier (lancer), à travers au sens de grâce à (par, grâce à), sur une base régulière (régulièrement), faire du sens (avoir du sens), et la virgule systématique avant le "et" final d'une énumération.

**Participe accroché en fin de phrase** : une proposition au participe présent ajoutée pour gonfler le propos (", permettant ainsi de...", ", garantissant...", ", ce qui témoigne de..."). Écrire une vraie phrase avec un sujet, ou couper. Corriger la construction : "offrant" à la place de "permettant" garde le même tic.

## Structures à éviter

1. **Double affirmation symétrique** : "Non seulement X, mais aussi Y."
2. **Liste de trois mécanique** : "X, Y et Z sont les trois piliers de..."
3. **Fausse concession** à poids égal : "Bien que X soit important, il ne faut pas négliger Y."
4. **Question rhétorique** suivie d'une réponse générique.
5. **Interpellation universelle** : "En tant que professionnel, vous savez que..."
6. **Transitions en série** : de plus, en outre, par ailleurs, cependant, toutefois, néanmoins.
7. **Passif sans source** : "Il a été démontré que...", "Des études montrent que...".
8. **Étiquette au-dessus d'un titre** : un petit libellé posé au-dessus d'un titre pour annoncer la rubrique ("Installation", "Le principe", "Pourquoi ça marche"). Il répète ce que le contenu montre déjà et signe une mise en page générée. Le supprimer, garder le titre seul.
9. **Rupture-écho** : une affirmation coupée en deux phrases dont la seconde reprend la première pour fabriquer un effet ("Se démarquer ne tient plus au volume. Ça tient à..." ; "Ce n'est pas un problème d'outil. C'est un problème de..."). La coupe n'apporte rien, elle imite la vivacité. Relier en une phrase : "ne tient plus au volume mais à...". Une phrase courte reste permise quand elle dit quelque chose de neuf, pas quand elle répète.
10. **Binôme parallèle** : deux propositions courtes coulées dans le même moule ("Le prof compte, la salle regarde."). La symétrie fait slogan et dit peu. Lui préférer un verbe concret qui décrit ce qui se passe ("Le prof la fait évoluer avec la salle.").
11. **Contre-pied elliptique** : une négation générale, puis un fragment qui la retourne ("Personne ne lit un chiffre au fond d'une salle. Une couleur, si."). C'est le "ce n'est pas X, c'est Y" déguisé. Écrire une seule phrase, quitte à assumer un registre parlé.
12. **Nuance hachée** : deux phrases sèches là où un "mais" suffisait ("Seule la jauge en cours tombe. Les points déjà gagnés restent acquis." devient "La jauge en cours tombe mais les points déjà gagnés restent acquis."), et la chute en fragment nominal ("Aucun plafond." devient ", sans plafond de points."). Relier avec le connecteur le plus simple.
13. **Fragment sans verbe en titre ou en promesse**, fréquent sur les visuels et les slides ("Ce format, dans vos cours ?", "Chaque jauge pleine, un point de plus"). Écrire une vraie phrase, une question entière ("Et si on appliquait ce format à vos cours ?"), un impératif ("Ajoutez cette jauge à vos propres cours."), ou une exclamation quand il y a de quoi.
14. **Opposition de décor**, sous toutes ses formes :
   - "X n'est pas Y, c'est Z" et "Ce n'est pas X. C'est Y." ("Un abonnement n'est pas un projet.")
   - "X, pas Y" ("Du terrain, pas de la théorie")
   - la négation suivie de sa reprise ("Le problème ne vient pas de la motivation. Il vient de l'organisation.")
   - "On ne X pas, on Y" ("Il n'analyse pas, il écrit.")
   - "X, c'est bien. Y, c'est mieux"
   - "Pas X : Y" et "Pas X, juste Y" ("Pas des mots-clés : des réponses.")
   - "X plutôt que Y" et "X au lieu de Y" quand Y n'existe que pour être rejeté (un avant et un après réellement vécus restent permis)

   Correction : affirmer directement ce qui est vrai, avec un verbe concret. "Ce qui vous coûte cher, c'est le temps que personne n'a pris pour brancher l'outil." La croyance à défaire n'a pas besoin d'être énoncée. Une vraie nuance reliée par "mais" reste permise (structure 12) : elle apporte une information, elle ne fabrique pas d'adversaire.

   Ce qui n'est pas visé : une négation qui informe ("les automatisations ne traitent jamais de données médicales"), une subordonnée négative ("des gens qui n'en font pas"), une condition ("tant qu'il n'a pas vos données"). Le test : si on retire la moitié niée, la phrase perd-elle une information ? Si non, c'était une opposition de décor.
15. **Étiquette suivie de deux-points en tête de phrase** : un groupe nominal suivi de deux-points prend la place du verbe et donne au texte un air de slide.
   - le décor ou le rôle : "Autour de la table : ...", "Mon rôle : ...", "L'objectif : ...", "Le contexte : ...", "Ma règle : ..."
   - le verdict : "Résultat : ...", "Bilan : ...", "Le problème : ...", "Spoiler : ...", "Concrètement : ...", "En clair : ..."
   - la variante en question : "Le résultat ? ...", "La différence ? ...", "Le secret ? ..."

   Correction : remettre un verbe conjugué. "Autour de la table, il y avait des...", "Mon rôle était de cadrer...", "Ce qui coince, c'est...". Ce qui n'est pas visé : les deux-points qui suivent une phrase complète pour annoncer une liste ou une explication, le "PS :", les lignes de métadonnées, les titres de document. Le test : avant les deux-points, y a-t-il un verbe conjugué ? Si non, réécrire.
16. **Révélation mise en scène** : le texte annonce ce qu'il va dire au lieu de le dire. "Et voici pourquoi.", "Mais ce n'est pas tout", "La réponse est simple :", "Une chose est sûre :", "Le vrai enjeu, c'est...", "C'est là que [outil] entre en jeu", "le détail qui change tout", "Ce que personne ne vous dit sur...", un intertitre en relative ("Le seuil qui déclenche la dépense"), la sincérité proclamée ("Soyons honnêtes :", "La vérité, c'est que"), la fin qui se dérobe ("Tout dépend de vos besoins") ou qui tourne à la morale ("Au-delà de la technologie, c'est une question de sens"). Donner l'information tout de suite, nommer le sujet dans l'intertitre ("Le seuil de dépense"), finir sur une position ou un critère chiffré.
17. **Morceau collé après une virgule** : un bout de phrase accroché derrière une virgule pour faire net, au lieu d'être construit dans la phrase.
   - un nom suivi d'un participe seul : "et ses cinq questions, résolues", "le même cas, recadré", "vos données, nettoyées" ;
   - une précision ajoutée en fin de phrase avec un rythme de comptage : "On retravaille un prompt sur un cas, en trois passes", "Une salle, un outil, une heure".

   Écrire la proposition entière avec un verbe ("et les réponses à ses cinq questions", "on recadre le même cas"). Le test : si le morceau après la virgule n'a pas de verbe conjugué et pourrait servir de légende de slide, réécrire. Une apposition qui nomme ("Marie, notre formatrice, ...") reste permise.
18. **Intertitre qui amorce une explication** au lieu de nommer la rubrique :
   - les relatives en "ce que" ou "ce qui" : "Ce que ça coûte", "Ce que ça change", "Ce qu'il faut retenir" ;
   - "Comment ça se passe", "Comment ça marche", "Pourquoi ça compte" ;
   - tout titre qui commence par "À" suivi d'un verbe : "À décider", "À retenir", "À noter".

   Correction : un nom sec choisi pour ce que la section contient ("Ce que ça coûte" devient "Coût", "Ce que ça apporte" devient "Gain", "Comment ça se passe en décembre" devient "Déroulé en décembre"). Dans le corps du texte, ces amorces restent sous surveillance : chercher chaque "Ce que ça", "Ce qui", "Pourquoi ça", "Comment ça" et chaque ligne qui commence par "À" suivi d'un verbe, et ne garder que celles qui portent une information dans une phrase complète ("Ce que ça coûte, c'est 5 minutes par classe" reste permis, sous réserve des structures 14 et 16). Dans un document de travail (note, rapport, fiche), l'intertitre est un nom sec ; sur un visuel ou une slide, la structure 13 s'applique et demande une vraie phrase.
19. **Tics de seconde génération** : ils restent dans un texte déjà nettoyé, parce que le modèle a remplacé une habitude par une autre. À chercher une fois les structures 1 à 18 traitées :
   - la fausse maxime : une phrase qui a la forme d'une vérité et que personne ne contesterait ("Un bon outil se fait oublier."). Le test : quelqu'un pourrait-il ne pas être d'accord ? Si non, la remplacer par le fait qu'elle évoque, ou la couper ;
   - la chute passe-partout : une dernière ligne équilibrée qui pourrait clore n'importe quelle page ("Parce que votre équipe mérite mieux."). Finir sur un chiffre, un nom, l'offre ou l'action ;
   - l'équilibre parfait : chaque section a un titre, deux phrases et trois puces. Laisser la section la plus forte s'allonger, la plus faible rétrécir ou partir ;
   - la précision réflexe : un chiffre rond ou une anecdote trop nette posés sur chaque affirmation. Chaque chiffre et chaque histoire doivent être réels et sourcés ; sinon, écrire [preuve à fournir].

   Vérification : relire la dernière ligne de chaque section et comparer la longueur des sections. Si elles font toutes à peu près la même taille, le texte est trop équilibré.

Les structures 9 à 18 ont un point commun : le modèle découpe en petits blocs symétriques et fabrique des contrastes pour imiter la vivacité, alors qu'une personne relie, précise, affirme. La phrase courte reste un outil, à sortir quand elle dit du neuf : si trois phrases de suite sont des fragments ou des binômes, en relier au moins deux.

## Ce qu'on met à la place

- **Du précis** : une entreprise nommée, un chiffre daté, un lieu réel, une source citée.
- **Une position** : "c'est une mauvaise idée", "personne ne fait ça correctement", "la plupart des conseils sur ce sujet sont inutiles".
- **Un rythme irrégulier** : une phrase de 4 mots après une longue, une digression, une liste de 2 éléments ou de 8.
- **Une structure imparfaite** : pas de parallélisme forcé, pas de sections égales, pas de conclusion qui répète l'introduction.
- **Un ancrage concret** : un détail de lieu, de moment ou de sensation réel, une anecdote qui comporte un échec ou une surprise.
- **Le test de portabilité** : une phrase qui passerait telle quelle chez un concurrent ou sur un autre sujet ("Nous plaçons l'humain au cœur de notre démarche") se réécrit avec ce que seul ce client ou cette mission permet de dire. Si aucun fait propre n'existe, le signaler plutôt que l'inventer.

## Garde-fou : ne pas surcorriger

Le second piège se voit autant que le premier. À force de fuir les tics, on en fabrique d'autres : fragments partout, avis tranché sans objet, phrase de trois mots toutes les quatre lignes, ponctuation qui casse au hasard. C'est la marque des outils de "réécriture humaine" bas de gamme.

- La rupture de rythme sert le sens. Si le propos tient mieux sans la phrase courte, elle part.
- L'opinion porte sur le sujet. Pas d'avis tranché pour faire vivant.
- Viser une variation naturelle : une personne cultivée écrit de façon irrégulière, sans casser ses phrases.
- Le test : relire. Si le texte sent l'effort pour paraître spontané, c'est raté autant qu'un texte trop lisse.

## Adapter au format

Les tics s'accumulent avec la longueur : un texte court passe, un long les additionne.

| Format | Consigne dominante |
|---|---|
| Email de prospection (5 à 10 lignes) | Une idée par phrase, aucune tournure d'entreprise, première ligne concrète. |
| Accroche de page d'accueil | Un verbe et un bénéfice concret. |
| Post sur un réseau social | Une ouverture qui accroche, un rythme heurté assumé, une vraie prise de position. |
| Article long | C'est là que les tics s'accumulent. Longueurs très variées, respirations, digression réelle, exemple daté. |
| Slide | Peu de phrases complètes : groupes nominaux, chiffres, verbes d'action, sous réserve des structures 13 et 17. |
| Proposition commerciale | Une position sur le sujet, jamais de provocation gratuite. Ton professionnel tenu, phrases vivantes et précises. |
| Courrier formel (administration, école, grand compte) | Une seule formule de politesse, jamais l'empilement "Restant à votre disposition... Dans l'attente de votre retour... Veuillez agréer...". La formule finale reprend l'appel ("Madame la Directrice," appelle "Je vous prie d'agréer, Madame la Directrice, ..."). "Espérant..., veuillez agréer" est fautif : le participe demande "je" ("Espérant..., je vous prie d'agréer"). Pour un email courant, "Cordialement," ou "Bien cordialement,". Un courrier trop sec passe pour impoli : garder la formule attendue, une fois. |
| CV | Expériences en groupes nominaux, sans "je" ("Animation d'un groupe de 10 personnes"). Les structures 15 et 17 ne s'appliquent pas à ces lignes. L'accroche peut garder la première personne. |

## Avant et après

> Avant : "Dans un monde où la concurrence est de plus en plus forte, il est crucial pour les entreprises de se démarquer grâce à une stratégie de contenu robuste et différenciante."

> Après : "Vos concurrents publient les mêmes articles que vous, écrits par les mêmes outils. Se démarquer ne tient plus au volume mais à ce que personne d'autre ne puisse écrire à votre place."

L'ouverture de contexte a disparu, deux mots creux (`crucial`, `robuste`) aussi, une affirmation vérifiable remplace une généralité, et le texte prend position. La seconde phrase est reliée ("ne tient plus au volume mais à...") : une première version disait "Ça ne tient plus au volume. Ça tient à..." et tombait dans la rupture-écho (structure 9).

## Signes typographiques

Toujours :
- Aucun tiret cadratin (`—`) : une virgule, un point-virgule ou des parenthèses.
- Pas de `→` pour simuler un raisonnement : écrire le raisonnement.
- Aucun point médian (`·`) **dans le corps du texte** pour empiler des fragments ("rapide · fiable · sur mesure") : une virgule, un point ou une vraie liste. Il reste permis sur une ligne de métadonnées (pied de page, signature, mentions), où il sépare des informations de même nature. Le test : s'il sépare des phrases ou des arguments, il part ; s'il sépare des coordonnées, il reste.
- Pas de puces hors d'une vraie liste pour hacher une phrase.
- Pas de gras sur 3 à 5 mots par paragraphe.
- Pas d'emojis décoratifs en tête de liste.
- Aucun reste de conversation avec un chatbot : `utm_source=chatgpt.com` ou `utm_source=openai` dans une adresse, `contentReference[oaicite:0]`, `turn0search0`, `【1†`, champs à remplir oubliés ("[Votre nom]", "[Entreprise]"). Les supprimer, puis revérifier l'affirmation à laquelle ils étaient accrochés.

### Exception : les emojis de repérage

L'interdiction vise l'emoji **décoratif**, qui orne une puce sans rien ajouter. Elle ne vise pas l'emoji **de repérage** dans un document fait pour être parcouru plutôt que lu (fiche pratique, mode d'emploi, guide client, aide-mémoire), à trois conditions :
1. **Un seul par titre**, jamais en série dans le corps du texte.
2. **Il porte du sens** : l'enveloppe pour écrire, l'alarme pour l'urgence. S'il pourrait être remplacé par n'importe quel autre, il est décoratif et part.
3. **Jamais dans un document formel** : devis, facture, contrat, proposition chiffrée, courrier officiel.

En HTML ou en PDF, placer l'emoji dans une pile de polices dédiée, sinon il s'affiche en carré ou en noir et blanc selon le lecteur : `font-family: "Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji", sans-serif`.

### Préférences typographiques, à choisir

Les conventions ci-dessous relèvent du goût de l'auteur ou de la charte du document. Par défaut, le skill suit la convention déjà en place dans le texte ; pour un texte neuf, la typographie française classique. L'utilisateur peut choisir le **profil clavier** dans sa demande ou dans ses instructions permanentes (CLAUDE.md).

| Point | Typographie française classique (par défaut) | Profil clavier |
|---|---|---|
| Guillemets | Chevrons « ... », avec espaces insécables | Droits "..." |
| Apostrophe | Courbe ou droite, une seule forme dans tout le texte | Droite ' |
| Nombres | Petits nombres en lettres dans un texte courant (le seuil varie selon les chartes), en chiffres devant une unité de mesure et pour les données | En chiffres dès 2, y compris en début de phrase et dans les titres ; restent en lettres "un", "une", les expressions figées ("en deux temps") et les citations |
| `%` et `€` | Espace insécable avant le signe ("75 %", "10 €") | Signe collé au chiffre ("75%", "10€") |
| Virgules | Usage courant | Légères : aucune virgule devant un complément court en fin de phrase, devant "parce que", ni devant "et", "mais", "puis", "ou" qui relient deux morceaux courts |

Le profil clavier part d'une idée simple : un texte tapé au clavier AZERTY porte les signes du clavier, et un texte plein de chevrons et d'espaces insécables sort souvent d'un traitement automatique. Cela ne prouve rien, dans un sens comme dans l'autre : Word et les téléphones posent ces signes tout seuls.

La cohérence prime sur le profil. Un texte qui mélange deux formes du même signe dans un paragraphe se voit tout de suite. Ne jamais convertir en masse un texte déjà publié sans demande explicite : le gain est faible et le risque de casse réel (un guillemet droit posé dans un attribut HTML le coupe en deux ; y écrire `&quot;`).

## Posture

- Écrire sans commenter sa façon d'écrire.
- Prendre position, sans ménager le sujet.
- Couper avant d'ajouter. Si un mot ne change pas le sens, il part.
- Si la consigne est trop vague pour écrire juste, demander la cible, le contexte, le ton voulu et la longueur.
- Pas de version "au cas où" ni de variantes non demandées.

## Place dans la chaîne

Ce skill écrit et retire les tics. La relecture finale (accords, ponctuation, coquilles, cohérence) passe par `/relecture-finale`, publié dans le même paquet. Ne pas faire son travail à sa place, ni compter sur lui pour rattraper un texte bâclé.

## Vérification avant de rendre

Avant de livrer, passer son propre texte au crible et corriger sans le commenter :

1. Aucun tiret cadratin. Aucun point médian dans le corps du texte.
2. Aucun mot du lexique creux, ni synonyme qui garde la même emphase.
3. Une seule forme de guillemets et d'apostrophe dans tout le texte, selon le profil choisi.
4. Aucune contraction orale.
5. **Rythme** : les longueurs de phrase varient-elles vraiment ? Si trois phrases de suite font la même taille, en changer une.
6. **Prévisibilité** : reste-t-il des passages où chaque mot est le plus attendu ? Les remplacer par un choix plus juste.
7. Au moins une position qui porte sur le sujet.
8. Pas de surcorrection : le texte ne sent pas l'effort pour paraître spontané.
9. **Découpage** : aucun binôme symétrique, aucun contre-pied en fragment, aucune nuance coupée en deux phrases là où un "mais" suffit, aucun titre ou promesse sans verbe (structures 10 à 13).
10. **Oppositions** : aucune opposition de décor (structure 14). Relire chaque négation : si elle ne sert qu'à préparer un "c'est", un "mais" de contraste ou une reprise, elle part.
11. **Deux-points** : avant chaque deux-points du corps du texte, un verbe conjugué (structure 15), hors "PS :", métadonnées et titres.
12. Aucune révélation mise en scène (structure 16), aucun reste de chatbot.
13. Aucun morceau collé après une virgule (structure 17).
14. **Intertitres** : dans un document de travail, aucun titre en "Ce que...", "Ce qui...", "Comment ça...", "Pourquoi ça..." ou "À" suivi d'un verbe (structure 18).
15. Si le profil clavier est choisi : nombres, `%`, `€` et virgules conformes au tableau.

Zéro occurrence pour les points 1 à 4 et 11 à 15, sinon réécrire avant de rendre. Les points 5 à 10 se jugent plus qu'ils ne se comptent.

Sur un texte anglais, cette vérification est remplacée par celle de `references/anglais.md`.

## Module EXHAUSTIVITÉ

- Traiter TOUTES les entrées : si N textes ou passages sont fournis, N sont traités. Interdit : "et ainsi de suite", "exemples représentatifs", "les principaux éléments".
- Avant de rendre, compter les entrées et les sorties ; si les nombres diffèrent, reprendre.
- Aucun champ à remplir, "TODO" ni section vide dans le livrable final.
- Ne jamais s'arrêter à mi-tâche pour proposer de continuer : rendre le résultat complet en une fois.
- Si la sortie complète ne tient pas en une fois, découper en lots et livrer TOUS les lots, jamais un échantillon présenté comme complet.
- Si des valeurs par défaut sont définies, les appliquer sans poser de question et signaler l'hypothèse à la fin. Exception : une action destructive ou irréversible demande toujours confirmation.

## Sources

La partie anglaise (`references/anglais.md`) reprend et adapte le skill [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) de Conor Bronsdon, sous licence MIT (copyright 2026 Conor Bronsdon) : ses 21 catégories et sa table de 43 remplacements. La relecture en deux passes et l'alignement sur un échantillon de l'auteur suivent la démarche de [humanizer](https://github.com/blader/humanizer), sous licence MIT. Deux règles françaises s'inspirent de skills publiés sous licence MIT : les calques de l'anglais de [le-unslop](https://github.com/painhardcore/le-unslop), la révélation mise en scène (structure 16) de [slopcheck-fr](https://github.com/tns-research/slopcheck-fr). Le reste est original.
