---
name: diagnostic-tics-ia
description: "Diagnostic chiffré des tics d'écriture IA d'un texte français : score sur 25, rapport qui cite chaque extrait et nomme son procédé, signes d'écriture humaine relevés, puis, sur demande, correction en 6 étapes. Sert à savoir quoi corriger avant de reprendre un texte avec ecrire-sans-tics-ia, ou à mesurer un texte avant et après. Déclenche pour /diagnostic-tics-ia, \"note ce texte sur 25\", \"ce texte sonne-t-il IA ?\", \"quels tics d'IA dans ce texte ?\", ou le diagnostic d'un texte suspect avant sa réécriture."
---

# Diagnostic des tics d'IA

Ce skill lit un texte français avec un œil d'éditeur et repère les formules, les structures et la typographie qui sentent le texte généré (ChatGPT, Claude, Gemini, Mistral, Copilot). Le score dit combien de procédés il contient, pas qui l'a écrit : une personne pressée en produit aussi, et un texte généré bien repris n'en garde aucun.

## Mode d'emploi (à afficher au lancement)

> **/diagnostic-tics-ia : combien de tics d'IA dans ce texte, et lesquels**
> - Collez le texte, ou donnez le chemin du fichier
> - Vous recevez un score sur 25, chaque extrait cité avec le nom de son procédé, et ce qui sonne humain
> - Ensuite, si vous le demandez, je corrige ; pour une réécriture complète, `/ecrire-sans-tics-ia`

Trois cas :
1. **Un texte est fourni** : produire le rapport de diagnostic.
2. **Une correction est demandée** : appliquer le protocole de correction.
3. **Rien n'est fourni** : demander le texte.

## Les procédés à repérer

### Lexique

**Adjectifs creux** : crucial, fondamental, essentiel, capital, vital, robuste, holistique, nuancé, multifacette, multidimensionnel, incontournable, optimal, pertinent, innovant, révolutionnaire.

**Verbes creux** : exploiter (au sens de tirer parti), leverager, naviguer (au sens figuré), appréhender, façonner, modeler, catalyser, orchestrer, déployer (une stratégie), booster, sublimer, optimiser.

**Jargon d'entreprise** : écosystème, paysage (concurrentiel, médiatique), paradigme, synergies, feuille de route, parties prenantes, valeur ajoutée, impact (non chiffré), trajectoire, dynamique, vecteur, levier.

**Formules d'introduction** : "Dans le monde d'aujourd'hui...", "À l'ère du numérique...", "Il est indéniable que...", "Force est de constater que...", "Il convient de noter que...", "Il est important de souligner que...", "Comme nous le savons tous...", "Dans le contexte actuel...", "Face aux défis contemporains...".

**Formules de clôture** : "En conclusion, nous pouvons affirmer que...", "Pour résumer les points clés...", "N'hésitez pas à me contacter...", "J'espère que cet article vous a été utile.", "Pour aller plus loin...", "L'avenir appartient à ceux qui...".

**Transitions mécaniques en série** : de plus, en outre, par ailleurs, cependant, toutefois, néanmoins, en effet, ainsi, il est donc clair que, dans cette optique, à cet égard, en ce sens.

**Tournures typiques du français généré** : "Il convient de", "Il y a lieu de", "Dans cette perspective", "À titre d'exemple", "Il est à noter que", "De surcroît", "Tant sur le plan X que sur le plan Y".

**Calques de l'anglais** : implémenter (mettre en œuvre), adresser un problème (traiter), supporter au sens de soutenir, challenger comme verbe, générer de la valeur, être aligné avec.

### Structures de phrase

1. **Double affirmation** : "Non seulement X, mais aussi Y.", toujours symétrique.
2. **Liste de trois** : "X, Y et Z sont les trois piliers de...". Les listes font 3 ou 5 éléments, rarement 4 ou 7.
3. **Fausse concession** : "Bien que X soit important, il ne faut pas négliger Y.", une nuance à poids égal qui ne tranche rien.
4. **Question rhétorique** : "Mais qu'est-ce que cela signifie concrètement ?", suivie d'une réponse générique.
5. **Interpellation universelle** : "En tant que professionnel, vous savez que...", vide et englobante.

**Passif sans source** : "Il a été démontré que...", "Il est généralement admis que...", "Des études montrent que...".

**Références absentes** : "Des études récentes", "Selon les experts du domaine", "La recherche a démontré", sans rien de vérifiable.

### Procédés rhétoriques

- **Ouverture flatteuse** : "Excellente question !", "C'est très pertinent", une validation avant la réponse.
- **Fausse nuance** : autant d'avantages que d'inconvénients, et une conclusion du type "la vérité est entre les deux".
- **Plan en entonnoir** : introduction générale, définition, trois parties égales, implications pratiques, conclusion qui répète l'introduction.
- **Conseils génériques** : "Fixez des objectifs SMART", "Communiquez clairement", "Mesurez vos résultats" ; vrais partout, utiles nulle part.
- **Empathie de façade** : "Nous comprenons que...", "Il est normal de se sentir...", "Vous n'êtes pas seul".

### Organisation du contenu

- Des listes partout : tout ce qui pourrait s'écrire en phrases devient une liste.
- Des listes de 3 à 7 éléments, jamais plus, jamais moins.
- Des intertitres en cascade : quatre niveaux de titres pour 800 mots.
- Un parallélisme forcé : sections de même longueur, symétrie parfaite.
- Aucune tension interne : une cohérence parfaite et lisse est elle-même suspecte.

### Typographie

Ces signes remplacent une vraie syntaxe par de la mise en forme. En masse, ils se voient tout de suite.

- `→` simule un raisonnement ("X → Y") sans l'écrire. Une personne écrit "donc", "ce qui donne", "d'où", ou tourne la phrase autrement.
- `—` le tiret cadratin, là où une virgule, un point-virgule ou des parenthèses feraient le même travail avec moins d'emphase.
- `•` une puce tapée à la main hors d'une vraie liste, pour découper une phrase en faux éléments.

### Registre administratif

Les modèles ont lu énormément de textes officiels et en font leur registre neutre.

- "Au sein de" : dans
- "Dans le cadre de" : pour, lors de, dans
- "En termes de" : sur, concernant, pour
- "En matière de" : sur, en, pour
- "À même de" : capable de, en mesure de
- "Afin de" : pour (les modèles choisissent presque toujours la forme longue)
- "Permettre de" employé à tout propos : rendre possible, faciliter, aider, autoriser

### Mise en forme

- Du gras sur 3 à 5 mots par paragraphe.
- Des emojis décoratifs en tête de liste (✅, 📌, 🎯, ⚠️). Exception : l'emoji de repérage, un par titre de section, dans un document fait pour être parcouru (fiche pratique, mode d'emploi, guide client). Jamais dans un document formel (devis, facture, contrat).
- Des sections "À retenir", "Points clés", "TL;DR" ou "FAQ" ajoutées d'office.
- Une longueur artificielle : la même idée reformulée en trois phrases.

### Signes d'écriture humaine absents

- Aucune anecdote avec un détail réel de lieu, de moment ou de sensation.
- Aucun échec vécu.
- Aucune opinion tranchée ("c'est une mauvaise idée", "je déteste cette approche").
- Aucune position qui divise.
- Aucun humour, aucune ironie, aucun second degré.
- Aucune rupture de rythme (pas de phrase de trois mots après une longue).
- Aucune digression.
- Aucune référence culturelle précise et datée.
- Aucune imperfection cohérente avec une personnalité.
- Une grammaire parfaite dans un registre uniformément moyen.

## Rapport de diagnostic

Pour chaque texte analysé :

**Score : X sur 25**, soit le nombre de procédés distincts relevés, plafonné à 25.
- 0 à 4 : peu de tics, texte vraisemblablement écrit ou bien repris par une personne
- 5 à 8 : plusieurs tics, à reprendre
- 9 et plus : texte généré peu ou pas repris

**Verdict** : PEU DE TICS, À REPRENDRE, ou GÉNÉRÉ PEU REPRIS.

**Procédés relevés.** Pour chacun, l'extrait exact et le nom du procédé :

> "extrait du texte" : [NOM DU PROCÉDÉ], explication courte

**Signes d'écriture humaine.** Ce qui va dans l'autre sens, cité de la même façon.

**Diagnostic.** Deux ou trois phrases : le procédé le plus visible, et la principale faiblesse du texte.

Le score mesure des procédés d'écriture. Il ne prouve pas qu'une IA a écrit le texte et ne doit jamais servir à accuser quelqu'un.

## Protocole de correction

Quand une correction est demandée :

1. **Retirer** les mots du lexique creux et les remplacer par des mots précis.
2. **Casser la structure** : entrer directement dans le sujet, supprimer l'introduction de contexte et la conclusion qui la répète.
3. **Mettre du précis** : une entreprise nommée à la place d'"une entreprise", une source citée à la place d'"une étude", un détail daté ou situé. Si l'information manque, la demander au lieu de l'inventer.
4. **Prendre position** : au moins une opinion nette, et plus de fausse nuance symétrique.
5. **Varier le rythme** : au moins une phrase de cinq mots ou moins, une digression, une liste imparfaite (2 éléments ou 8).
6. **Lire à voix haute** : ce qui sonne faux à l'oral sonne encore généré.

Après correction, dire en quelques lignes ce qui a changé et pourquoi.

## Posture

- Direct, sans diplomatie inutile.
- Ne pas valider un texte plein de tics pour ménager son auteur.
- Citer les extraits exacts, jamais une paraphrase.
- Distinguer "généré, non repris", "généré, repris" et "écrit par une personne, avec des tics".
- Si le texte est trop court pour conclure, le dire et demander plus de matière.

## Module EXHAUSTIVITÉ

- Traiter TOUS les textes fournis : si N textes sont donnés, N rapports sont rendus.
- Avant de rendre, compter les entrées et les sorties ; si les nombres diffèrent, reprendre.
- Aucun champ à remplir, "TODO" ni section vide dans le rapport.
- Ne jamais s'arrêter à mi-tâche pour proposer de continuer.
