# Outils pour TOGAFrance

_Une version anglaise est disponible : [README.md](./README.md)_

Ce dossier rassemble tous les scripts, modèles et outils d’automatisation conçus pour aider les contributeurs et les territoires pilotes à produire, structurer ou synchroniser les documents et retours d’expérience dans le cadre de TOGAFrance.

---

## Que pouvez-vous proposer ici ?

- **Scripts d’automatisation** : conversion Markdown → PDF/Docx/Xlsx, synchronisation de traductions, générateurs de modèles, etc.
- **Modèles de documents** : en Markdown, Docx, Excel, pour aider les territoires à créer facilement leurs fichiers.
- **Autres outils** : tout utilitaire facilitant le partage, le reporting ou la visualisation des données liées au projet.

---

## Dossiers

- `scripts/` : scripts et programmes d’automatisation ou de traitement
- `templates/` : modèles de rapports ou documents (simples et collaboratifs)
- `qualite/` : contrôles automatiques du dépôt (liens, traçabilité, lisibilité)
- `fake-data/` : territoires fictifs pour s’exercer (et pour le jeu)

Chaque script ou outil doit contenir un `README.md` dans son propre sous-dossier.

---

## Documentation & Kit de démarrage

Tous les modèles et exemples sont accessibles ici :

- `/tools/templates/` : modèles de reporting communautaires (simples et adaptables)
- `/pilots-territories/` : cas concrets, dont l’exemple complet du feu rouge
- `/documentation/` : guides de référence, glossaires et livret pratique complet

**Bonnes pratiques :**
- Choisissez le modèle le plus adapté à votre contexte (léger ou TOGAF strict)
- Pour les documents officiels ou institutionnels, partez des modèles de `/tools/templates/` et de l’exemple complet de `/pilots-territories/`
- Pensez à remplir le numéro de version, l’auteur et le changelog si le document est formel
- Consultez `NAMING-CONVENTION-FR.md` pour les règles de nommage
- En cas de doute, posez une question ou proposez une amélioration !

---

## Comment contribuer ?

1. Proposez un script ou un modèle dans le bon sous-dossier
2. Ajoutez une courte documentation ou un en-tête commenté à votre fichier
3. Mettez à jour ce README si votre outil mérite d’être mis en avant
4. Partagez vos retours ou idées via une issue ou une pull request

---

## Besoins & Pistes

État : ✅ opérationnel · 🧩 squelette à construire (le fichier existe, la logique reste à écrire)

- ✅ [Contrôle qualité : liens, traçabilité, lisibilité](./qualite/README-FR.md)
- 🧩 [Conversion Markdown → PDF / DOCX / XLSX](./scripts/generate-pdf/README-FR.md)
- 🧩 [Traduction automatique (Markdown ↔️ EN/FR)](./scripts/translate-md/README-FR.md)
- 🧩 [Génération de modèles (diagnostic, plan, retour)](./scripts/generate-template/README-FR.md)
- ✅ [Outils de rédaction](./writing-tools/README-FR.md)
- ✅ [Exemples et données factices](./fake-data/README-FR.md)
- 🧩 [Surveillance inter-repo (Programme2027 → TOGAFrance)](./scripts/sync-programme2027/README-FR.md)
- 🧩 [Matrice des rôles ou catalogue d’acteurs](./scripts/generate-role-matrix/README-FR.md)
- 🧩 [Diagrammes automatiques](./scripts/generate-diagrams/README-FR.md)
- 🧩 [Assistant IA (style TOGAFrance)](./scripts/tf-assistant/README-FR.md)


_Même un brouillon, un prototype ou un travail en cours sont les bienvenus. Co-construisons les communs._

---
