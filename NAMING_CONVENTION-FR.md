# Convention de nommage des fichiers et dossiers

_Version française : ce document existe aussi en anglais : [NAMING-CONVENTION.md](./NAMING-CONVENTION.md)_

---

## Règles générales

- **Utilisez uniquement des minuscules et des tirets (`-`)** pour séparer les mots.  
  _Exemple : `example-pilot`, `diagnostic.md`, `action-plan.md`_
- **Pas d’espaces, pas d’accents, pas de caractères spéciaux** (sauf tiret et underscore si besoin).
- Pour tous les fichiers bilingues, **ajoutez le code langue en suffixe** :
  - Anglais : pas de suffixe (par défaut)
  - Français : `-FR` avant l’extension
  - _Exemple : `README.md` (EN), `README-FR.md` (FR) ; `diagnostic.md` (EN), `diagnostic-FR.md` (FR)_
- **Gardez les extensions de fichiers en minuscules** (`.md`, `.docx`, `.py`, etc.)
- **Sous-dossiers pour les pilotes/territoires** : utilisez `pilots-territories/<lieu-ou-groupe>-<année>/`

---

## Exemples

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