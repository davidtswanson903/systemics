BOOK_PDF=build/systemics-book.pdf
BOOK_MAIN=main.tex

.PHONY: pdf watch clean

pdf:
	latexmk -pdf -jobname=systemics-book -output-directory=build $(BOOK_MAIN)

watch:
	latexmk -pdf -pvc -jobname=systemics-book -output-directory=build $(BOOK_MAIN)

clean:
	latexmk -C -jobname=systemics-book -output-directory=build $(BOOK_MAIN)
	rm -rf build
