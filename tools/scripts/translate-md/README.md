# 🌐 Script `translate-md-to-fr`

This folder contains a **Python script** (to be completed) intended to **automatically translate Markdown files into French** as part of the **TOGAFrance** project.

---

## 🧭 Purpose

This script aims to:

- Identify all `.md` files in a given directory
- Translate their content into French
- Preserve the Markdown structure (headings, lists, code blocks, etc.)
- Avoid re-translating files that are already translated
- Offer flexible configuration via arguments or external file

---

## 📁 Folder structure

```
tools/scripts/
├── translate-md-to-fr.py   # Main script (to be developed)
└── README.md               # This documentation
```

---

## 🛠️ Expected contributions

The script is currently a **starting point**. You can contribute by:

- Integrating a translation API or library (e.g., DeepL, Google Translate, OpenAI, Argos Translate)
- Preserving code blocks and Markdown formatting
- Implementing batch processing
- Adding a command-line interface (`argparse`)
- Documenting options and dependencies in a `requirements.txt`

---

## 🧪 Example usage (planned)

```bash
python translate-md-to-fr.py --input ./docs/EN/ --output ./docs/FR/
```

---

## ⚙️ Planned features

- Automatic detection of source language
- Selection of translation engine
- Option to process one or more files
- Interactive or silent mode
- Logging of errors and translation stats

---

## 📜 License

Free to use and modify.  
All contributions must respect the spirit of the **TOGAFrance** project: clarity, rigor, accessibility.

---

## 🧠 About

This script is part of the collaborative tooling and automated documentation effort for **TOGAFrance**.
