# Tools for TOGAFrance

_A French version is available: [README-FR.md](./README-FR.md)_

This folder gathers all scripts, templates, and automation tools designed to help contributors and pilot territories with TOGAFrance documentation and feedback.

---

## What can you contribute here?

- **Automation scripts:** e.g., Markdown to PDF/Docx/Xlsx, translation synchronizers, template generators, etc.
- **Templates:** Markdown, Docx, Excel, to help new pilots create their documents easily.
- **Other tools:** any utility facilitating sharing, reporting, or data visualization for the project.

---

## Folders

- `scripts/`: code/scripts for automation or processing
- `templates/`: document or report templates (community-friendly, lightweight)
- `qualite/`: automated repository checks (links, traceability, readability)
- `fake-data/`: fictional territories for practice (and for the game)

Each script/tool should include its own `README.md` inside its folder.

---

## Documentation & Starter Kit

All main templates and examples are available in:

- `/tools/templates/` : community reporting templates (simple, adaptable)
- `/pilots-territories/` : real-world cases, including the full traffic-light example
- `/documentation/` : reference guides, glossaries, and the full practical handbook

**Best practices:**
- Use the template best suited to your context (lightweight or strict TOGAF format)
- For official or institutional documents, start from `/tools/templates/` and the full example in `/pilots-territories/`
- Always fill in version, author, and changelog if using a formal document
- Check `NAMING-CONVENTION.md` for file naming rules
- When in doubt, ask or propose an improvement!

---

## How to contribute?

1. Propose a script or template in the relevant subfolder.
2. Add a short documentation or comment header to your file.
3. Update this README if your tool deserves to be highlighted.
4. Share feedback or improvement ideas via issue or pull request.

---

## Needs & Ideas

Status: ✅ working · 🧩 skeleton to build (the file exists, the logic is still to write)

- ✅ [Quality checks: links, traceability, readability](./qualite/README.md)
- 🧩 [Markdown → PDF / DOCX / XLSX](./scripts/generate-pdf/README.md)
- 🧩 [Automatic translation scripts (Markdown ↔️ EN/FR)](./scripts/translate-md/README.md)
- 🧩 [Template generators](./scripts/generate-template/README.md)
- ✅ [Writing helpers](./writing-tools/README.md)
- ✅ [Fake/example data](./fake-data/README.md)
- 🧩 [Cross-repo monitoring script](./scripts/sync-programme2027/README.md)
- 🧩 [Role matrix / actor catalog](./scripts/generate-role-matrix/README.md)
- 🧩 [Auto-generated diagrams](./scripts/generate-diagrams/README.md)
- 🧩 [AI assistant (TOGAFrance style)](./scripts/tf-assistant/README.md)



_Even a draft, prototype, or work-in-progress is welcome. Let’s co-build the commons._


---
