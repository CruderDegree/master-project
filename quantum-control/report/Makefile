FINALNAME = Extended-Quantum-Control-Report-3rd-Edition

all: report.pdf
	cp -f $< $(FINALNAME).pdf

report.pdf: report.tex thebibliography.bib
	pdflatex $<
	pdflatex $<
	bibtex $<
	pdflatex $<

.PHONY: clean
clean:
	rm -f *.aux *.out
