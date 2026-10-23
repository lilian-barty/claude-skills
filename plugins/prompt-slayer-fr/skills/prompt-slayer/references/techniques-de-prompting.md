# Techniques de prompting : pourquoi les modules fonctionnent

Référence de Prompt Slayer. Elle explique ce que fait chaque module A à H et quelle technique ajouter quand un prompt rate un de ses tests. Elle ne change ni le format de réponse ni la règle d'or : on construit le prompt, on ne fait pas le travail.

## 1. Des exemples plutôt que des règles (few-shot)

Un modèle imite mieux qu'il n'obéit. Deux à cinq paires entrée et sortie montrent le comportement attendu plus sûrement qu'un paragraphe de consignes.

À utiliser pour :
- une sortie qui doit garder exactement la même forme (classement, extraction, JSON) ;
- un niveau de détail ou un ton difficile à décrire ;
- un cas limite qu'on veut voir traité d'une façon précise.

Le dosage dépend de la tâche. Deux exemples suffisent souvent à fixer un format ; un jugement nuancé en demande quatre ou cinq. Chaque exemple coûte des tokens à chaque appel, ce qui compte dans une automatisation qui tourne mille fois par jour.

Exemple, le tri des emails entrants d'une agence :

```
Classe chaque email dans une seule catégorie : devis, réclamation, candidature, autre.
Réponds par un objet JSON.

Email : "Bonjour, pourriez-vous m'envoyer un tarif pour refaire notre site vitrine ?"
Réponse : {"categorie": "devis", "urgence": "normale"}

Email : "Ça fait 3 semaines que la facture n° 2041 est fausse et personne ne répond."
Réponse : {"categorie": "réclamation", "urgence": "haute"}

Email : "Je vous joins mon CV pour le poste de chef de projet."
Réponse : {"categorie": "candidature", "urgence": "basse"}

Email : {{ email }}
Réponse :
```

Les erreurs habituelles :
- des exemples éloignés de la vraie tâche : le modèle copie leur forme et rate l'intention ;
- des exemples tous du même type : glisser au moins un cas limite (ici, la réclamation agacée) ;
- trop d'exemples pour la fenêtre du modèle, qui finit par oublier la consigne de départ.

Dans Prompt Slayer, c'est la variante "few-shot". Pour Claude, ranger les exemples dans une balise `<exemples>`.

## 2. Faire raisonner avant de conclure

Demander les étapes du raisonnement avant la réponse améliore les tâches où une erreur intermédiaire fausse tout le reste : calculs, rapprochements, diagnostics, décisions qu'on veut pouvoir contrôler.

Deux façons de faire :
- la consigne courte ("réfléchis étape par étape avant de répondre") ;
- les étapes imposées, plus fiables, parce qu'elles disent quoi vérifier.

Exemple, le rapprochement d'une facture et d'un bon de commande :

```
Dis si cette facture peut être payée.

Vérifie dans cet ordre :
1. Le fournisseur est-il le même sur les deux documents ?
2. Chaque ligne facturée figure-t-elle sur le bon de commande ?
3. Les quantités et les prix unitaires sont-ils identiques ?
4. Le total de la facture est-il égal à la somme des lignes ?
Puis conclus par "payable" ou "à bloquer", avec la raison en une phrase.

Bon de commande : {{ bon }}
Facture : {{ facture }}
```

À adapter selon la cible :
- les modèles dits "de raisonnement" réfléchissent déjà en interne. Imposer les étapes (module D) reste utile ; exiger qu'ils affichent tout leur raisonnement l'est beaucoup moins, et allonge la sortie ;
- dans une automatisation, le raisonnement ne doit jamais polluer la sortie. Le demander dans un champ JSON prévu pour cela (`"verifications"`) ou pas du tout.

## 3. Améliorer par versions

Un bon prompt se trouve rarement du premier coup. On part simple, on mesure sur les mêmes entrées, on resserre.

Exemple, le compte rendu d'une réunion :

```
Version 1 : "Fais le compte rendu de cette réunion."
Ce qui sort : une longueur qui varie de 5 à 40 lignes, et les décisions noyées dans le récit.

Version 2 : "Liste les décisions prises, puis les actions avec leur responsable."
Ce qui sort : une structure stable, mais les actions sans échéance sont inventées.

Version 3 : la même consigne, plus "si aucune échéance n'est dite, écris 'non fixée'".
Ce qui sort : stable, fidèle, et plus aucune date inventée.
```

Les règles qui font gagner du temps :
- une seule modification par version, sinon on ne sait pas laquelle a marché ;
- les mêmes entrées à chaque version, cas limites compris (c'est le rôle du plan de test en 3 cas) ;
- quand l'enjeu le justifie, deux variantes comparées sur les mêmes entrées ;
- en production, une surveillance dans le temps : un changement du modèle sous-jacent casse parfois un prompt qui marchait.

Dans un outil qui exécute lui-même le travail (Claude Code, un agent), on peut clore le prompt par une boucle de relecture : 2 ou 3 relecteurs, chacun chargé d'un angle (structure, fond, respect de la demande), critiquent le livrable au regard de la demande de départ ; l'agent corrige et resoumet, 5 passages au plus. Chaque passage coûte du temps et des tokens, et le gain n'a pas été mesuré ici : à réserver aux livrables qui le valent.

## 4. N'ajouter de la complexité que si le test l'exige

Quatre niveaux, à gravir seulement quand le niveau du dessous échoue :

1. La consigne seule : "Fais le compte rendu de cette réunion."
2. Des contraintes : "En 10 lignes au plus, décisions d'abord."
3. Une méthode : "Repère les décisions, puis les actions et leurs responsables, puis rédige."
4. Des exemples : un ou deux comptes rendus modèles.

Correspondance avec les modules : le niveau 1 est le module B, le niveau 2 les modules E et F, le niveau 3 le module D, le niveau 4 des exemples dans le module C ou la variante few-shot. Le mode FAST s'arrête au niveau 1 ou 2 ; le mode PRO monte aussi haut que les critères l'exigent.

## 5. L'ordre des blocs

L'ordre qui donne les sorties les plus stables :

```
Contexte permanent -> consigne -> exemples -> données -> format de sortie
```

Deux conséquences :
- les données longues (document, transcription, export) se placent après les consignes et se délimitent nettement (balises, blocs, guillemets), sinon le modèle prend une phrase des données pour une consigne ;
- quand l'entrée est longue, rappeler le format de sortie à la toute fin : c'est ce que le modèle lit en dernier.

## 6. Les gabarits

Un prompt réutilisable se compose d'une structure fixe, de variables et, si besoin, de passages qui ne s'affichent que dans certains cas. On cesse de réécrire, et des tâches voisines restent cohérentes entre elles.

Exemple, la réponse à un avis client, dans un nœud n8n :

```
Rédige une réponse à cet avis laissé sur {{ $json.plateforme }}.
Note donnée : {{ $json.note }} sur 5.
Avis : """{{ $json.texte }}"""

Si la note est de 3 ou moins, reconnais le problème précis cité et propose un contact direct.
Si la note est de 4 ou 5, remercie en reprenant un détail de l'avis.
80 mots au plus, signé "{{ $json.signature }}".
```

Dans Prompt Slayer, les variables en `[MAJUSCULES]` du livrable client jouent ce rôle. Dans n8n ou Make, elles deviennent des expressions (`{{ $json.champ }}` dans n8n, le mappage de champs dans Make) : documenter celles qui peuvent arriver vides, et ce que le prompt doit faire dans ce cas.

## 7. Le system prompt

Le system prompt porte ce qui ne change pas d'un échange à l'autre : rôle, niveau d'expertise, format de sortie, règles de sécurité. Les messages de l'utilisateur portent le contenu variable.

Exemple, l'assistant interne d'un service RH :

```
Tu réponds aux questions des salariés sur les congés et les absences, à partir du règlement fourni entre les balises <reglement>.

Règles :
- Cite l'article du règlement sur lequel tu t'appuies.
- Si le règlement ne répond pas, dis-le et oriente vers le service RH ; n'invente jamais une règle.
- Ne donne jamais d'information sur un autre salarié.
- Si la question sort des congés et absences, réponds que tu ne traites que ce sujet.

Format : la réponse en 3 phrases au plus, puis "Article : ...".
```

Pour un system prompt persistant (GPT personnalisé, agent), toujours prévoir, en plus des règles de la section "Adaptation par outil cible" du SKILL.md, ce qu'il fait quand la demande sort de son périmètre et ce qu'il fait quand une information manque.

## 8. Prévoir l'échec dans le prompt

Un prompt solide dit quoi faire quand les choses tournent mal :
- une consigne de repli ("si l'email ne contient pas de numéro de commande, renvoie null") ;
- un niveau de confiance sur les réponses incertaines ;
- plusieurs interprétations quand la demande est ambiguë, en conversation seulement : en automatisation, on applique la valeur par défaut ;
- une manière explicite de signaler ce qui manque, plutôt que de l'inventer.

C'est le cœur des modules SAFE et AUTOMATION.

## 9. Diagnostiquer un agent ou un GPT qui dérive

Quand l'utilisateur apporte un prompt existant qui se comporte mal, chercher dans cet ordre :

| Symptôme | Cause probable | Remède |
|---|---|---|
| Sortie dont la forme varie | Format décrit, jamais montré | Exemples (section 1) et format rappelé en fin de prompt (section 5) |
| Réponse superficielle à un problème complexe | Aucune méthode imposée | Étapes de vérification (section 2) |
| Faits ou sources inventés | Aucune règle pour l'incertitude | Module SAFE et consignes de repli (section 8) |
| Données prises pour des consignes | Données non délimitées | Balises ou blocs, ordre des blocs (section 5) |
| Sort de son rôle au fil de l'échange | Pas de comportement hors périmètre | Section 7 |
| Casse le workflow en aval | Texte libre au lieu de JSON, questions posées | Module AUTOMATION |
| Marchait, ne marche plus | Modèle ou entrées qui ont changé | Rejouer le plan de test, changer une chose à la fois (section 3) |

Le livrable reste un prompt corrigé, jamais l'exécution de la tâche.

## 10. Habitudes qui paient

1. Écrire précis : un prompt vague donne des sorties irrégulières.
2. Montrer : un exemple vaut mieux qu'une description.
3. Tester sur des entrées variées et représentatives, pas seulement sur le cas idéal.
4. Itérer souvent, par petites touches : un mot changé suffit parfois.
5. En production, mesurer au lieu de supposer.
6. Versionner les prompts comme du code : une date par version, ce qui a changé et pourquoi.
7. Écrire l'intention pour la personne qui maintiendra le prompt (c'est la note de maintenance du livrable client).

## 11. Erreurs fréquentes

- Commencer par un prompt complexe avant d'avoir essayé le simple.
- Des exemples qui ne correspondent pas à la tâche.
- Trop d'exemples ou de données pour la fenêtre du modèle.
- Une consigne qui laisse place à deux lectures.
- Ne tester que le cas nominal.
