# Exemplars

This directory contains executable Systemics theory instances (“exemplars”).

Each exemplar folder is *literate + executable*:

- `theory.py`: instantiation using the `systemics` library under `lib/`
- `narrative.tex`: human-readable explanation included by the book
- `build/report.tex`: generated LaTeX report (gitignored)
- `build/law_report.json`: generated structured results (gitignored)

Build:

- `make exemplars` (repo root)
- or run `python tools/build_exemplar.py exemplars/EX1_minimal_algebra`
