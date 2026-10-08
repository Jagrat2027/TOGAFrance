# TOGAFrance – Chapitre 11 : Catalogue d'indicateurs humains

_Version anglaise disponible ici : [11-human-indicators.md](./11-human-indicators.md)_

---

La méthode refuse « les indicateurs vides de sens humain ». Ce catalogue propose l'inverse : des indicateurs qui mesurent ce que vivent les personnes, chacun avec une façon simple de le mesurer.

Un bon indicateur TOGAFrance répond à trois questions :

1. **Qu'est-ce que ça change dans la vie de quelqu'un ?** Si personne ne le sent, ce n'est pas un indicateur humain.
2. **Qui peut le mesurer, et comment ?** Un indicateur sans protocole n'existe pas.
3. **À partir de quel seuil agit-on ?** Chaque indicateur suivi doit pouvoir alimenter une fiche de réversibilité (livrable 13).

---

## Le catalogue

| Code | Indicateur | Ce qu'il dit de la vie réelle | Comment le mesurer | Fréquence |
| --- | --- | --- | --- | --- |
| H-01 | **Temps réel d'une démarche** | Combien de temps une personne perd pour obtenir ce à quoi elle a droit | Chronométrer 10 parcours d'usagers réels, du premier contact à la réponse | Trimestrielle |
| H-02 | **Délai de résolution d'un problème** | Combien de temps on reste dans la difficulté après l'avoir signalée | Date du signalement → date de résolution, dans le registre des signalements | Mensuelle |
| H-03 | **Nombre d'étapes d'une démarche** | La complexité ressentie | Compter les écrans, formulaires, déplacements et pièces demandées pour un parcours type | À chaque changement |
| H-04 | **Taux de non-recours** | Combien de personnes renoncent à un droit | Ayants droit estimés − bénéficiaires, rapporté aux ayants droit (avec le service concerné) | Annuelle |
| H-05 | **Part des démarches possibles sans numérique** | Qui est laissé de côté par le tout-écran | Pour chaque démarche : existe-t-il un guichet, un téléphone ou un courrier ? (oui / non) | Annuelle |
| H-06 | **Satisfaction des usagers** | Le vécu, dit par les personnes elles-mêmes | Question unique « Ce service vous a-t-il aidé ? » (oui / en partie / non), papier et QR code | Continue |
| H-07 | **Incidents et mises en danger** | La sécurité ressentie et réelle | Registre partagé : police, école, riverains, agents | Mensuelle |
| H-08 | **Sens au travail des agents** | Si ceux qui font le service y croient encore | Question unique anonyme « Votre travail sert-il les gens ? » (échelle de 1 à 5) | Semestrielle |
| H-09 | **Retours d'usagers suivis d'effet** | Si la parole sert à quelque chose | Nombre de retours ayant conduit à une modification ÷ nombre de retours reçus | Trimestrielle |
| H-10 | **Compréhension d'un document** | Si le langage clair est vraiment clair | 5 personnes lisent le document, puis le résument : combien l'ont compris ? | À chaque version |

---

## Règles d'usage

- **Peu d'indicateurs, bien suivis.** Trois indicateurs mesurés chaque mois valent mieux que quinze oubliés.
- **Toujours une version qualitative.** Un chiffre sans témoignage ne dit pas *pourquoi*. Accompagnez chaque mesure de deux ou trois paroles d'usagers, anonymisées.
- **Mesurer avant d'agir.** Relevez l'indicateur avant la transformation : sans point de départ, impossible de dire si l'on a progressé.
- **Pas de classement entre territoires.** Ces indicateurs servent à s'améliorer, pas à sanctionner. Un indicateur utilisé pour punir finit toujours par être manipulé.
- **Protéger les personnes.** Aucune donnée nominative ; les enquêtes sont anonymes et facultatives.

---

## Relier les indicateurs au reste de la méthode

Chaque indicateur suivi dans un projet reçoit un identifiant local (`IND-01`, `IND-02`…) et se rattache :

- à une ou plusieurs **exigences** (livrable 7), qu'il permet de vérifier ;
- éventuellement à une **fiche de réversibilité** (livrable 13), avec un seuil de déclenchement ;
- au **cahier de veille** (livrable 14), où il est relevé dans le temps.

Ces liens sont écrits dans un fichier `tracabilite.yaml` à la racine du projet pilote. Le contrôle automatique du dépôt vérifie que la chaîne est complète : voir l'exemple du [feu rouge devant une école](../pilots-territories/00_example_territory/00_example_city/00_example_feurouge.md/tracabilite.yaml) et [`tools/qualite`](../tools/qualite/README-FR.md).

---

_Chapitre précédent : [10-appendices-FR.md](./10-appendices-FR.md)_
