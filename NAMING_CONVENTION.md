# Naming Convention for Files and Folders

_A French version is available: [NAMING_CONVENTION-FR.md](./NAMING_CONVENTION-FR.md)_

---

## General Rules

- **Use lowercase letters** and dashes (`-`) to separate words in file and folder names.  
  _Example: `example-pilot`, `diagnostic.md`, `action-plan.md`_
- **No spaces, no accents, no special characters** (except dash and underscore if needed).
- For all paired files, **append the language code as a suffix**:
  - English: no suffix (default)  
  - French: `-FR` before the extension
  - _Example: `README.md` (EN), `README-FR.md` (FR); `diagnostic.md` (EN), `diagnostic-FR.md` (FR)_
- **Keep file extensions in lowercase** (`.md`, `.docx`, `.py`, etc.)
- **Subfolders for pilots/territories**: use `pilots-territories/<location-or-group>-<year>/`

---

## Examples

/pilots-territories/
    example-pilot/
        diagnostic.md
        diagnostic-FR.md
        action-plan.md
        action-plan-FR.md
        experience-report.md
        experience-report-FR.md
        README.md
        README-FR.md


templates/
    template-report.md
    template-report-FR.md