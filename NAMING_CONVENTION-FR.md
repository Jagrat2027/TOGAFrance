# Convention de nommage des fichiers et dossiers

_Version française : ce document existe aussi en anglais : [NAMING_CONVENTION.md](./NAMING_CONVENTION.md)_

---

## Règles générales

- Utilisez des **underscores `_`** pour séparer les mots dans les noms de fichiers.  
  Exemples : `action_plan.md`, `experience_report.md`, `template_report.md`

- Utilisez un **tiret `-`** juste avant l’extension du fichier pour indiquer la version linguistique.  
  Exemples :  
  - Anglais (par défaut) : `action_plan.md`  
  - Français : `action_plan-FR.md`  
  - Allemand (futur) : `action_plan-DE.md`

- Gardez les extensions en minuscules et cohérentes (`.md`, `.docx`, `.py`, etc.).

- Pour les noms de dossiers, utilisez des **tirets `-`** pour séparer les mots.  
  Exemples : `pilots-territories`, `tools/scripts`

---

## Exemples

/pilots-territories/
    example-pilot/
        diagnostic.md
        diagnostic-FR.md
        action_plan.md
        action_plan-FR.md
        experience_report.md
        experience_report-FR.md
        README.md
        README-FR.md


templates/
    template_report.md
    template_report-FR.md