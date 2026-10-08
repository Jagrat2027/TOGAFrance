# Quality checks

_French version: [README-FR.md](./README-FR.md)_

`verifier.py` re-reads the whole repository on every change, through the "Qualité TOGAFrance" GitHub Action. It applies the method's own principles to the method: clarity, transmission, shared memory.

## What fails the check (error)

- **A broken internal link** in any Markdown file.
- **An incomplete traceability chain** in a pilot project that has a `tracabilite.yaml`:
  - a requirement in deliverable 7 missing from the file (or the reverse);
  - a mandatory requirement with no way to verify it;
  - a requirement linked to no need;
  - a reversibility trigger (deliverable 13) with no indicator, or no threshold;
  - an indicator pointing to a code missing from the [catalogue of human indicators](../../documentation/11-human-indicators.md).

## What only warns

- An optional requirement with no verification, an indicator linked to nothing, a need with no requirement.
- **The 10-year-old challenge**: a French deliverable or chapter whose Kandel–Moles readability score is below 40. The higher the score, the easier the text. The full score table appears in the Action summary.

`--strict` makes warnings blocking.

## Usage

```
pip install pyyaml
python3 tools/qualite/verifier.py
```

## Tracing a pilot project

Copy the [`tracabilite.yaml` from the traffic-light example](../../pilots-territories/00_example_territory/00_example_city/00_example_feurouge.md/tracabilite.yaml), then:

1. give each requirement in deliverable 7 an identifier (`EX-01`…) and each trigger in deliverable 13 (`REV-01`…);
2. describe needs, indicators and links in the file;
3. run the check and fill in what it reports.

## Known limit

The readability score counts syllables approximately. It is a signal, not a verdict: the real measure remains indicator H-10 in the catalogue — have five people read the document.
