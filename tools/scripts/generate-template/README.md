# 🧩 Script `generate-template`

This script is used to **automatically generate standardized templates** for the official TOGAFrance deliverables, based on the document structures defined in [`./livrables`](../../livrables).

It allows contributors to create **empty but structured files** ready to be filled in, in various formats such as Markdown (`.md`), Word (`.docx`), or Excel (`.xlsx`).

---

## 📁 Reference: `./livrables` folder

The [`./livrables`](../../livrables) directory contains the **full specification** of TOGAFrance deliverables: diagnostic reports, action plans, feedback reports, etc.

This script automates the creation of working templates for those documents, in order to:

- ensure structural consistency across all contributions
- simplify onboarding of new collaborators
- bootstrap documents with ready-made section headers

---

## 🛠️ Expected contributions

- Multi-format generation: `.md`, `.docx`, `.xlsx`
- Pre-filled titles, sections, and required fields
- Bilingual output (FR / EN)
- Configurable via `config.yaml`

---

## 🧪 Example usage

```bash
python generate-template.py --type diagnostic --format md
python generate-template.py --type feedback --format docx --lang en
```

---

## 📜 License

Free to use and modify.  
Please follow the TOGAFrance editorial structure in any contribution.
