PDF=out/systemics.pdf
MAIN=tex/main.tex

BOOK_PDF=book/build/systemics-book.pdf
BOOK_MAIN=book/main.tex

.PHONY: pdf watch clean book book-clean lib-test check exemplars exemplar-ex1

pdf:
	latexmk -pdf -jobname=systemics -output-directory=out $(MAIN)

watch:
	latexmk -pdf -pvc -jobname=systemics -output-directory=out $(MAIN)

book:
	latexmk -pdf -jobname=systemics-book -output-directory=book/build $(BOOK_MAIN)

lib-test:
	cd lib && python -m pytest -q

exemplars:
	python tools/build_all_exemplars.py

exemplar-ex1:
	python tools/build_exemplar.py exemplars/EX1_minimal_algebra

check: exemplars book lib-test

clean:
	latexmk -C -jobname=systemics -output-directory=out $(MAIN)
	rm -rf out

book-clean:
	latexmk -C -jobname=systemics-book -output-directory=book/build $(BOOK_MAIN)
	rm -rf book/build
