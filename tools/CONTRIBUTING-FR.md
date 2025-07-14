# Contributions aux outils TOGAFrance

TOGAFrance n'est pas seulement une méthode : c'est aussi un espace de fabrication collective.  
Si vous aimez automatiser, structurer, ou simplifier la vie des contributeurs — vous êtes au bon endroit.

---

## 🔧 Besoins identifiés & Idées ouvertes

- ✅ **Scripts de conversion Markdown → PDF / DOCX / XLSX**  
  Pour produire rapidement des documents partageables à partir des fichiers `.md`.

- ✅ **Traduction automatique intelligente (Markdown ↔️ EN/FR)**  
  Avec détection de changement et mise à jour automatique des sections traduites.

- 🧩 **Générateurs de modèles**  
  Produire facilement des templates de diagnostics, plans d’action ou bilans d’expérience (en Markdown, Word, Excel).

- 🔍 **Checklists et guides contributeurs**  
  Pour aider les nouveaux contributeurs à bien formuler, structurer et documenter leurs apports.

- 📄 **Données d’exemple et cas fictifs**  
  Permettent de tester les outils avec des données réalistes (ex : commune test, livrables fictifs, etc.).

- 🔁 **Surveillance inter-dépôts (Programme2027 → TOGAFrance)**  
  Détecter automatiquement un changement majeur dans le Programme, et créer une *issue* dans TOGAFrance si cela impacte la vision, les principes ou les livrables.

- 🧪 **Générateurs de matrices ou catalogues**  
  À partir de fichiers YAML/JSON : catalogue des besoins, des parties prenantes, ou des rôles.

- 🔗 **Diagrammes dynamiques**  
  Générer automatiquement des schémas ADM ou des représentations des flux et rôles.

- 🧠 **Assistant IA ou prompts de rédaction**  
  Pour aider à rédiger dans l’esprit TOGAFrance, avec clarté, bienveillance et lisibilité.

---

## 🤝 Toute contribution compte

- Même un début de script.
- Même une idée partielle.
- Même une correction sur un outil existant.

> On ne construit pas pour briller.  
> On construit pour transmettre.

---

## 🛠️ Règles pratiques pour les contributions techniques

> Ces règles visent à garantir que les scripts et outils soient clairs, utilisables et maintenables.

### 📁 Structure des dossiers

- Chaque script ou outil doit être placé dans un sous-dossier de `/tools/scripts/`  
  Exemple : `/tools/scripts/generate-pdf/`, `/tools/scripts/translate-md/`

- Ajoutez un fichier `README.md` dans le dossier de l’outil, contenant :
  - l’objectif du script
  - un ou plusieurs exemples d’utilisation
  - la description des entrées/sorties
  - les dépendances nécessaires (modules Python, outils CLI…)

---

### 📄 Nommage des fichiers

- Utilisez des **noms clairs et explicites**, en anglais de préférence  
  ✅ `generate.py`, `sync.py`, `translate.py`  
  ❌ `script1.py`, `code_final.py`, `truc.sh`

- Évitez les espaces, majuscules ou accents dans les noms de fichiers ou de dossiers  
  ✅ `generate-pdf/`  
  ❌ `Générateur PDF/`

---

### 🧪 Exécution et tests

- Le script doit :
  - pouvoir s’exécuter seul (`python script.py fichier.md`)
  - ne pas planter si une entrée est manquante (afficher une aide plutôt)
  - documenter les dépendances (`pip install ...` ou équivalent)

- Si le script utilise une API externe (DeepL, GitHub...), indiquez-le clairement dans le `README.md` et **ne jamais** commettre de clé API.

---

### 🤝 Proposer un outil

Pour proposer un outil :

1. Créez un sous-dossier dans `tools/scripts/` pour votre outil
2. Ajoutez un `README.md` documenté
3. Vérifiez que le script fonctionne sans erreur
4. Ouvrez une pull request ou une issue pour expliquer ce que fait l’outil

> Même un début de script est bienvenu. On améliore ensemble.

---

Tu peux proposer ton idée ou ton outil via une [issue](https://github.com/Jagrat2027/TOGAFrance/issues/new/choose) ou un [pull request](https://github.com/Jagrat2027/TOGAFrance/pulls).
