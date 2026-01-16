# Systemics

Monorepo containing:

- `book/`: LaTeX handbook (modular, multi-file)
- `lib/`: Python meta-framework library for defining Systemics theory instances

(An earlier modular LaTeX layout is still present under `tex/`.)

## Build

- `make book` builds `book/build/systemics-book.pdf`
- `make lib-test` runs python tests
- `make check` runs both

Legacy:

- `make pdf` builds `out/systemics.pdf` from `tex/main.tex`
