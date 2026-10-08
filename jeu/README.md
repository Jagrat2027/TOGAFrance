# Le Cycle — apprendre TOGAFrance en jouant

**Jeu coopératif · 2 à 5 joueurs · 60 à 90 minutes · dès 12 ans**

Vous êtes l'équipe qui accompagne un territoire fictif dans sa transformation : Pays-Silence, Port-Lumière, Hautes-Combes… Chacun incarne un rôle de la méthode (le Passeur, le Gardien, le Veilleur, le Bâtisseur, le Relieur) et l'équipe traverse ensemble les 8 phases du cycle.

En chemin, des crises, des signaux faibles à ne pas manquer, des raccourcis tentants, et des seuils d'alerte où il faut choisir : s'obstiner, ou revenir en arrière en le disant.

Personne ne gagne seul. Si la Confiance des habitants tombe à zéro, tout le monde perd.

## Pour jouer

1. Imprimez [cartes-a-imprimer.html](./cartes-a-imprimer.html) (A4, à 100 %), puis découpez les 35 cartes.
2. Lisez les [règles](./regles.md) : 5 minutes.
3. Prévoyez des jetons (pièces, haricots…) et une feuille pour la piste de Confiance.

Toutes les cartes sont aussi lisibles en ligne : [cartes.md](./cartes.md).

## À qui il sert

- **Une réunion de quartier ou un conseil municipal** : 90 minutes pour comprendre la méthode sans un mot de jargon.
- **Une classe** (collège, lycée, enseignement civique) : chaque groupe joue un territoire, puis on compare les choix.
- **Une équipe d'agents publics** : la variante « Vrai territoire » transforme la partie en premier diagnostic.

## Modifier le jeu

Les cartes Rôle et Événement sont dans [cartes.yaml](./cartes.yaml) ; les territoires viennent des [données factices](../tools/fake-data/README-FR.md). Après une modification :

```
pip install pyyaml
python3 jeu/generer_cartes.py
```

Proposez une carte, une variante ou un retour de partie par issue ou pull request : le jeu s'améliore avec ceux qui y jouent.
