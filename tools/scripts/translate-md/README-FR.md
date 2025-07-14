# 🌐 Script `translate-md-to-fr`

Ce dossier contient un **script Python** (encore à compléter) destiné à **traduire automatiquement les fichiers Markdown en français** dans le cadre du projet **TOGAFrance**.

---

## 🧭 Objectif

Ce script vise à :

- Identifier tous les fichiers `.md` d’un répertoire donné
- Traduire leur contenu en français
- Conserver la structure Markdown (titres, listes, blocs de code, etc.)
- Éviter de retraduire des fichiers déjà traduits
- Proposer une configuration souple via arguments ou fichier externe

---

## 📁 Structure du dossier

```
tools/scripts/
├── translate-md-to-fr.py   # Script principal (à développer)
└── README.md               # Cette documentation
```

---

## 🛠️ Contribution attendue

Le script est pour l’instant un **point de départ**. Vous pouvez contribuer en :

- Intégrant une API ou une bibliothèque de traduction (ex : DeepL, Google Translate, OpenAI, Argos Translate)
- Préservant les blocs de code et le balisage Markdown
- Implémentant un traitement par lot
- Ajoutant une interface ligne de commande (`argparse`)
- Documentant les options et dépendances dans un `requirements.txt`

---

## 🧪 Exemple de fonctionnement (à terme)

```bash
python translate-md-to-fr.py --input ./docs/EN/ --output ./docs/FR/
```

---

## ⚙️ Options envisagées

- Détection automatique de la langue source
- Définition du moteur de traduction utilisé
- Choix d’un ou plusieurs fichiers en entrée
- Mode interactif ou silencieux
- Journalisation des erreurs et statistiques de traduction

---

## 📜 Licence

Libre d’usage et de modification.  
Toute contribution doit respecter l’esprit du projet **TOGAFrance** : clarté, rigueur, accessibilité.

---

## 🧠 À propos

Ce script fait partie des outils de travail collaboratif et de production documentaire automatisée pour **TOGAFrance**.
