# 📄 Script `generate-pdf`

This folder contains a **Python script** (to be completed) designed to **automatically generate PDF files from Markdown documents** used in the **TOGAFrance** project.

---

## 🧭 Purpose

This script aims to:

- Convert one or more `.md` files into `.pdf`
- Apply a unified style (via CSS/HTML or engines like WeasyPrint, Pandoc, etc.)
- Provide a simple command-line interface
- Centralize configuration through a `config.yaml` file

The goal is to **streamline the publication** of documents (chapters, summaries, notes) in a clean, readable format consistent with the project's visual identity.

---

## 📁 Folder structure

```
generate-pdf/
├── generate-pdf.py     # Main script (to be developed)
├── config.yaml         # Configuration file (styles, options, paths)
└── README.md           # This documentation
```

---

## 🛠️ Expected contributions

The script is currently a **skeleton**. You are welcome to contribute by:

- Implementing Markdown → PDF conversion using tools such as:
  - [`WeasyPrint`](https://weasyprint.org/)
  - [`pdfkit`](https://pypi.org/project/pdfkit/)
  - [`Pandoc`](https://pandoc.org/)
- Adding HTML or CSS templates for styling
- Enabling batch conversions (`*.md`)
- Managing command-line options via `argparse`
- Writing a `requirements.txt` with dependencies

---

## 🧪 Example usage (planned)

Single file conversion:

```bash
python generate-pdf.py --input ../docs/01_document_de_vision.md --output ./01_document_de_vision.pdf
```

Batch conversion:

```bash
python generate-pdf.py --input ../docs/ --output ./pdf/
```

---

## ⚙️ `config.yaml` file

The `config.yaml` file will allow:

- Defining the CSS theme or HTML template
- Setting PDF metadata (title, author, date)
- Specifying default input/output directories
- Enabling or disabling options such as:
  - table of contents
  - pagination
  - headers or footers

---

## 📜 License

Free to use and modify.  
All contributions must respect the spirit of the **TOGAFrance** project: transparency, simplicity, accessibility.

---

## 🧠 About

This script is part of the broader effort to automate the publication of the **TOGAFrance** programme.  
Please respect the structure and philosophy of the project.
