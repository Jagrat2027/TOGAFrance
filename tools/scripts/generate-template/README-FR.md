# 🧩 Script `generate-template`

Ce script permet de **générer automatiquement les modèles de livrables TOGAFrance** à partir des structures définies dans le dossier [`/livrables`](../../../livrables).

Il s'agit d'un outil de production rapide de **fichiers vides mais structurés**, prêts à être remplis par les contributeurs, dans différents formats : Markdown (`.md`), Word (`.docx`), Excel (`.xlsx`).

---

## 📁 Référence : dossier `./livrables`

Le dossier [`/livrables`](../../../livrables) contient la **description complète** des livrables attendus : diagnostics, plans d’action, rapports de retour, etc.

Le script `generate-template.py` propose une **version automatisée** de ces squelettes, pour :

- uniformiser la structure des documents produits
- faciliter la prise en main par de nouveaux contributeurs
- initier rapidement des fiches de travail en local

---

## 🛠️ Contributions attendues

- Génération multi-format : `.md`, `.docx`, `.xlsx`
- Intégration de sections, titres, champs prédéfinis
- Support multilingue (FR / EN)
- Paramétrage via un `config.yaml`

---

## 🧪 Exemple d’utilisation

```bash
python generate-template.py --type diagnostic --format md
python generate-template.py --type retour --format docx --lang en
```

---

## 📜 Licence

Libre d’usage et de modification.  
Respectez la structure éditoriale TOGAFrance pour toute contribution.
