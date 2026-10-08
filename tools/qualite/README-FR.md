# Contrôle qualité

_Version anglaise : [README.md](./README.md)_

`verifier.py` relit tout le dépôt à chaque modification, grâce à la GitHub Action « Qualité TOGAFrance ». Il applique à la méthode ses propres principes : clarté, transmission, mémoire partagée.

## Ce qui bloque (erreur)

- **Un lien interne cassé** dans n'importe quel fichier Markdown.
- **Une chaîne de traçabilité incomplète** dans un projet pilote qui a un `tracabilite.yaml` :
  - une exigence présente au livrable 7 mais absente du fichier (ou l'inverse) ;
  - une exigence obligatoire sans aucun moyen de vérification ;
  - une exigence rattachée à aucun besoin ;
  - un seuil de réversibilité (livrable 13) sans indicateur, ou sans seuil ;
  - un indicateur qui renvoie à un code absent du [catalogue d'indicateurs humains](../../documentation/11-indicateurs-humains-FR.md).

## Ce qui avertit sans bloquer

- Une exigence optionnelle sans vérification, un indicateur relié à rien, un besoin sans exigence.
- **Le défi des 10 ans** : un livrable ou un chapitre en français dont le score de lisibilité de Kandel et Moles est inférieur à 40. Plus le score est haut, plus le texte est facile. Le tableau complet des scores s'affiche dans le résumé de l'Action.

`--strict` rend les avertissements bloquants.

## Utiliser

```
pip install pyyaml
python3 tools/qualite/verifier.py
```

## Tracer un projet pilote

Copier [`tracabilite.yaml` de l'exemple du feu rouge](../../pilots-territories/00_example_territory/00_example_city/00_example_feurouge.md/tracabilite.yaml), puis :

1. donner un identifiant à chaque exigence du livrable 7 (`EX-01`…) et à chaque seuil du livrable 13 (`REV-01`…) ;
2. décrire les besoins, les indicateurs et les liens dans le fichier ;
3. lancer le contrôle et compléter ce qu'il signale.

## Limite connue

Le score de lisibilité compte les syllabes de façon approchée. C'est un signal, pas un verdict : la vraie mesure reste l'indicateur H-10 du catalogue, faire lire le document à cinq personnes.
