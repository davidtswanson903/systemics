#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

latexmk -pdf -jobname=systemics-book -output-directory=book/build book/main.tex
