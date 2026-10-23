# Skills Claude Code pour travailler avec l'IA

[English](README.md) · **Français**

Des skills pour [Claude Code](https://claude.com/claude-code), que j'ai écrits pour mon propre travail et dont je me sers tous les jours. Le premier conçoit des prompts pour d'autres IA et pour les automatisations. Les trois autres servent à écrire en français avec l'IA : le premier mesure les tics d'un texte généré, le deuxième les retire, le troisième fait la relecture finale.

| Plugin | Langue | Skills | Rôle |
|---|---|---|---|
| `prompt-slayer-fr` | français | `/prompt-slayer` | Fabrique un prompt prêt à coller dans ChatGPT, Claude, Perplexity, Midjourney, un nœud n8n, un module Make ou un GPT personnalisé, avec une version portable et un plan de test en 3 cas. Ne fait jamais la tâche lui-même. |
| `prompt-slayer` | anglais | `/prompt-slayer` | Le même skill, en anglais. |
| `ecriture-fr` | français (et anglais pour `/ecrire-sans-tics-ia`) | `/diagnostic-tics-ia`, `/ecrire-sans-tics-ia`, `/relecture-finale` | Écrire et relire en français : noter et retirer les tics d'IA, puis corriger fautes et typographie et contrôler la cohérence d'un paquet de documents. |

## Sommaire

- [Prompt Slayer](#prompt-slayer)
- [Diagnostic des tics d'IA](#diagnostic-des-tics-dia)
- [Écrire sans tics d'IA](#écrire-sans-tics-dia)
- [Relecture finale](#relecture-finale)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Limites](#limites)
- [Structure du dépôt](#structure-du-dépôt)
- [Sources](#sources)
- [Auteur](#auteur)

## Prompt Slayer

Les prompts que je vois échouer cassent presque toujours aux mêmes endroits : un format décrit mais jamais montré, aucune consigne quand une information manque, rien sur la conduite à tenir hors sujet. Prompt Slayer construit le prompt autour de ces points de rupture, puis vous donne trois tests pour le vérifier avant de vous y fier.

Pour une question ponctuelle dans ChatGPT, il est trop lourd : une consigne claire de deux lignes suffit. Il sert quand le prompt doit tourner seul, durer ou être remis à quelqu'un.

Le skill a une règle qu'il ne transgresse jamais : **il ne fait pas le travail.** Demandez-lui une fiche produit et vous recevez le prompt qui écrira de bonnes fiches produit, prêt à coller dans l'outil de votre choix.

À chaque demande, il rend :

1. l'objectif reformulé en une phrase ;
2. un diagnostic : type de tâche, endroit où le prompt sera exécuté, complexité, risque, critères de réussite ;
3. une question si une information critique manque, sinon les hypothèses retenues ;
4. le **prompt cible**, réglé pour l'outil que vous avez nommé ;
5. un **prompt portable**, utilisable sur n'importe quel modèle ;
6. des variantes quand elles servent (compacte, prudente, few-shot) ;
7. un **plan de test** : un cas nominal, un cas limite et un cas hors périmètre, chacun avec l'entrée exacte et ce à quoi ressemble une bonne réponse ;
8. une astuce applicable tout de suite.

L'endroit où le prompt sera exécuté le change davantage que le choix du modèle :

| Contexte | Ce que le prompt doit prévoir |
|---|---|
| Conversation | Une personne peut reformuler, le prompt peut donc poser des questions. |
| System prompt persistant (GPT personnalisé, agent) | Les cas limites sans personne pour aider, les demandes hors sujet, les tentatives d'extraction du prompt. |
| Automatisation (n8n, Make, appel d'API) | Personne dans la boucle : sortie JSON stricte, aucune question, entrées sales, objet d'erreur JSON plutôt que du texte libre. |
| Livrable pour un client | Quelqu'un d'autre le maintiendra : variables documentées, réglages d'installation, les trois tests, une note de maintenance. |

Le skill est livré avec une référence sur les techniques de prompting (`references/techniques-de-prompting.md`) : des exemples plutôt que des règles, les étapes de raisonnement, l'amélioration par versions, l'ordre des blocs, les gabarits, le system prompt, la gestion de l'échec, et un tableau symptôme, cause, remède pour réparer un agent ou un GPT qui dérive.

## Diagnostic des tics d'IA

`/diagnostic-tics-ia` lit un texte français et compte ses tics d'écriture IA : lexique creux, formules d'ouverture et de clôture, structures de phrase, procédés rhétoriques, mise en forme, typographie. Il rend un score sur 25, cite chaque extrait avec le nom de son procédé et relève aussi ce qui sonne humain. Sur demande, il corrige en 6 étapes ; pour une reprise complète, on passe à `/ecrire-sans-tics-ia`.

Le score compte des procédés d'écriture. Il ne dit pas qui a écrit le texte et ne doit jamais servir à accuser quelqu'un.

## Écrire sans tics d'IA

`/ecrire-sans-tics-ia` écrit un texte neuf, ou reprend un texte existant, pour qu'il ne porte plus les tics des textes générés. Il aide à mieux écrire avec l'IA et n'a pas été conçu pour cacher qu'on l'a utilisée ni pour tromper un détecteur.

Un texte généré se reconnaît d'abord à deux propriétés : chaque mot est celui qu'on attendait, et toutes les phrases ont la même longueur. Le skill travaille sur ces deux leviers, puis sur ce qui se voit en surface :

- un lexique creux à remplacer par des faits (crucial, robuste, écosystème, levier, "il convient de noter") ;
- 19 structures à éviter, dont l'opposition de décor ("ce n'est pas X, c'est Y" et ses variantes), la rupture-écho, le binôme symétrique, l'étiquette suivie de deux-points ("Résultat : ..."), la révélation mise en scène ("Et voici pourquoi.") et les tics qui restent une fois les premiers corrigés ;
- la typographie : aucun tiret cadratin, pas de flèche à la place d'un raisonnement, pas de point médian pour empiler des fragments ;
- un garde-fou contre la surcorrection, qui produit d'autres tics (fragments partout, avis tranchés sans objet).

Sur un texte existant, il retire les tics sans changer ni le sens ni les faits.

Il détecte la langue. Sur un texte anglais, il applique 21 catégories de procédés et une table de 43 remplacements, adaptées du skill [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing), puis une relecture en deux passes. Sur un fichier HTML, il cherche les tics par recherche textuelle avant de lire, pour ne rien rater dans les longues pages.

### Le profil typographique

Certaines règles relèvent du goût plus que des tics d'IA. Par défaut, les deux skills suivent la convention déjà en place dans le texte, ou la typographie française classique pour un texte neuf. Vous pouvez demander le **profil clavier** :

| Point | Typographie française classique (par défaut) | Profil clavier |
|---|---|---|
| Guillemets | « ... » | "..." |
| Nombres | Petits nombres en lettres | En chiffres dès 2 |
| `%` et `€` | "75 %", "10 €" | "75%", "10€" |
| Virgules | Usage courant | Légères, pas de virgule devant un complément court en fin de phrase |

Pour l'appliquer à chaque fois, ajoutez une ligne dans votre CLAUDE.md : "Typographie : profil clavier."

## Relecture finale

`/relecture-finale` corrige les fautes d'un texte français ou anglais sans toucher à son style : accords, conjugaison, coquilles, ponctuation, pronoms, répétitions involontaires, typographie, cohérence interne. Une phrase lourde mais juste est signalée, sans être réécrite. Chaque correction est notée dans un journal (avant, après, motif).

| Ce qu'on lui donne | Ce qu'il rend |
|---|---|
| Un texte collé | Le texte corrigé et le journal |
| Un fichier (.docx, .md, .txt, .html, .pdf) | Une copie `UPDATED_<nom>`, l'original intact ; dans un dépôt git, le fichier corrigé sur place |
| Le document d'un tiers | Une version Word en suivi des modifications, chaque correction à accepter ou refuser |
| Plusieurs documents liés | Le mode cohérence |

### Le mode cohérence

Sur un paquet de documents qui partagent des chiffres et des décisions (une étude et ses annexes, des fiches et leurs PDF, une présentation et ses notes, une proposition et son devis), la relecture à l'œil ne suffit pas. Sur un paquet de 7 documents annoncés "tous cohérents", ce contrôle a trouvé 108 écarts : des décisions corrigées dans un document et pas dans les autres, et des corrections qui en avaient abîmé d'autres.

Le mode cohérence travaille en trois couches :

| Couche | Ce qu'elle attrape |
|---|---|
| Registre des faits (`registre.yaml`) | Chaque chiffre et chaque décision, sa valeur juste, ses anciennes valeurs interdites |
| Script de contrôle (`controle.py`) | Une ancienne valeur encore présente, une valeur juste disparue d'un document, une règle de style enfreinte |
| Instantané | Tout paragraphe modifié depuis la dernière validation sans que ce soit prévu : une régression possible |

Le script lit le Markdown, le texte brut, le HTML (attributs `aria-label` compris), le PDF et les présentations en HTML, notes de l'orateur comprises. Un relecteur ne s'occupe plus ensuite que du sens. Un auto-test de 11 contrôles vérifie que chaque couche réagit.

## Installation

### Prérequis

- [Claude Code](https://claude.com/claude-code)
- Pour le mode cohérence de `/relecture-finale` seulement : Python 3 avec PyYAML (`pip install pyyaml`), et `pdftotext` (Poppler) pour lire les PDF.

### Avec le gestionnaire de plugins de Claude Code

```
/plugin marketplace add lilian-barty/claude-skills
/plugin install prompt-slayer-fr@lilian-barty-skills
/plugin install ecriture-fr@lilian-barty-skills
```

Puis redémarrez Claude Code. La version anglaise de Prompt Slayer s'installe avec `prompt-slayer@lilian-barty-skills` ; inutile d'installer les deux.

### Installation manuelle

Copiez le dossier d'un skill, par exemple `plugins/ecriture-fr/skills/relecture-finale`, dans `~/.claude/skills/`.

### Vérification

Pour le script du mode cohérence :

```
python ~/.claude/skills/relecture-finale/scripts/auto_test.py
```

Le résultat attendu est "11/11 contrôles passés". Après une installation par plugin, le script se trouve dans `~/.claude/plugins/cache/lilian-barty-skills/ecriture-fr/<version>/skills/relecture-finale/scripts/`.

## Utilisation

Dans Claude Code :

```
/prompt-slayer un system prompt pour un assistant qui ne répond qu'à partir de notre FAQ
/diagnostic-tics-ia note ce texte sur 25
/ecrire-sans-tics-ia relis ce post LinkedIn
/relecture-finale rapport.docx
```

Une demande en langage courant fonctionne aussi : "fais-moi un prompt pour Midjourney", "enlève les tics d'IA de ce texte", "corrige les fautes", "vérifie que tout est cohérent entre ces documents".

## Limites

- Prompt Slayer construit et teste les prompts sur le papier : il ne les exécute pas sur le modèle cible. Le plan de test est fait pour que vous le lanciez.
- Les modèles changent à chaque version. Les conseils propres à chaque outil reflètent les pratiques actuelles et se vérifient sur un modèle inconnu.
- `/ecrire-sans-tics-ia` ne garantit pas qu'un texte "passe pour humain" et n'a pas été conçu pour cela. Il retire des procédés d'écriture ; il n'invente ni faits ni anecdotes pour remplir.
- `/relecture-finale` ne juge ni la mise en page ni les graphiques. Le script du mode cohérence ne voit que ce qui est inscrit dans le registre ; la relecture de sens reste nécessaire.
- Les skills fonctionnent dans Claude Code. Le script du mode cohérence demande Python sur votre machine.

## Structure du dépôt

```
claude-skills/
├── .claude-plugin/
│   └── marketplace.json            la marketplace et ses trois plugins
├── plugins/
│   ├── prompt-slayer/              plugin anglais
│   │   ├── .claude-plugin/         manifeste du plugin
│   │   └── skills/prompt-slayer/
│   │       ├── SKILL.md            consignes que suit Claude
│   │       └── references/
│   │           └── prompting-techniques.md
│   ├── prompt-slayer-fr/           plugin français, même structure
│   └── ecriture-fr/                plugin d'écriture en français
│       └── skills/
│           ├── diagnostic-tics-ia/SKILL.md
│           ├── ecrire-sans-tics-ia/
│           │   ├── SKILL.md
│           │   └── references/anglais.md     règles pour l'anglais
│           └── relecture-finale/
│               ├── SKILL.md
│               ├── references/coherence-paquet.md
│               └── scripts/        controle.py et son auto-test
├── CHANGELOG.md
├── LICENSE
├── README.md                       version anglaise
└── README.fr.md                    cette page
```

## Sources

- Les règles anglaises de `/ecrire-sans-tics-ia` adaptent [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) de Conor Bronsdon (licence MIT, copyright 2026 Conor Bronsdon).
- Sa relecture en deux passes suit la démarche de [humanizer](https://github.com/blader/humanizer) (licence MIT).
- Deux de ses règles françaises s'inspirent de [le-unslop](https://github.com/painhardcore/le-unslop) et de [slopcheck-fr](https://github.com/tns-research/slopcheck-fr) (licence MIT).

Le reste est original.

## Auteur

Lilian Barty-Christophe, consultant en adoption de l'IA et automatisation, à Paris. J'aide des équipes à adopter l'IA et je construis les outils qu'elles adoptent : prompts, automatisations, petites applications.

Ces skills viennent de ce travail. Je passe par Prompt Slayer pour écrire les prompts des automatisations et des GPTs personnalisés, et chaque texte que je publie passe par les deux skills d'écriture. Deux autres de mes skills ont leur propre dépôt : [skill-refacto](https://github.com/lilian-barty/skill-refacto) (refactorisation prouvée) et [skill-tdah](https://github.com/lilian-barty/skill-tdah).

Site : [lilian-barty.fr](https://www.lilian-barty.fr/)

## Licence

[MIT](LICENSE)
