# 📄 Script `generate-pdf`

Ce dossier contient un **script Python** (encore à compléter) destiné à **générer automatiquement des fichiers PDF à partir de documents Markdown** utilisés dans le projet **TOGAFrance**.

---

## 🧭 Objectif

Ce script vise à :

- Convertir un ou plusieurs fichiers `.md` en `.pdf`
- Appliquer un style unifié (via CSS/HTML ou moteur comme WeasyPrint, Pandoc, etc.)
- Offrir une interface simple en ligne de commande
- Centraliser la configuration via un fichier `config.yaml`

L'objectif est de **faciliter la publication** de documents (chapitres, synthèses, notes) dans un format lisible, propre et cohérent avec l’identité visuelle du projet.

---

## 📁 Structure du dossier

```
generate-pdf/
├── generate-pdf.py     # Script principal (à développer)
├── config.yaml         # Fichier de configuration (styles, options, chemins)
└── README.md           # Cette documentation
```

---

## 🛠️ Contribution attendue

Le script est pour l’instant un **squelette**. Vous pouvez contribuer en :

- Implémentant la conversion Markdown → PDF avec un outil comme :
  - [`WeasyPrint`](https://weasyprint.org/)
  - [`pdfkit`](https://pypi.org/project/pdfkit/)
  - [`Pandoc`](https://pandoc.org/)
- Ajoutant un système de templates HTML ou CSS
- Permettant des conversions par lot (`*.md`)
- Gérant les options via la ligne de commande (`argparse`)
- Rédigeant un `requirements.txt` avec les dépendances

---

## 🧪 Exemple de fonctionnement (à terme)

Conversion d’un seul fichier :

```bash
python generate-pdf.py --input ../docs/01_document_de_vision.md --output ./01_document_de_vision.pdf
```

Conversion par lot :

```bash
python generate-pdf.py --input ../docs/ --output ./pdf/
```

---

## ⚙️ Fichier `config.yaml`

Le fichier `config.yaml` permettra de :

- Définir le thème CSS ou le template HTML
- Spécifier les métadonnées PDF (titre, auteur, date)
- Choisir les répertoires d’entrée/sortie par défaut
- Activer ou désactiver certaines options comme :
  - la table des matières
  - la pagination
  - les en-têtes ou pieds de page

---

## 📜 Licence

Libre d’usage et de modification.  
Toute contribution doit respecter l’esprit du projet **TOGAFrance** : transparence, sobriété, accessibilité.

---

## 🧠 À propos

Ce script fait partie de l’effort global de publication automatisée du programme **TOGAFrance**.  
Merci de respecter la structure et la philosophie du projet.
