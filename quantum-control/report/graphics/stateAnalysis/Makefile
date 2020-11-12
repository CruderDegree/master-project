BETADATA = beta-20.csv beta-10.csv beta0.csv beta10.csv beta20.csv
GRIDDATA = grid64.csv grid128.csv grid256.csv grid512.csv grid1024.csv
FIGS = GroundstateGrid.pdf GroundstateBeta.pdf ExcitedstateGrid.pdf ExcitedstateBeta.pdf Energylevels.pdf Energydifference.pdf
LIBSRC = ../../../lib

all: $(FIGS)

# Grid spacing figs

GroundstateGrid.pdf: groundstateGrid.py $(GRIDDATA)
	python3.8 $<

ExcitedstateGrid.pdf: excitedstateGrid.py $(GRIDDATA)
	python3.8 $<

# High-res beta figs
GroundstateBeta.pdf: groundstateBeta.py $(BETADATA)
	python3.8 $<

ExcitedstateBeta.pdf: excitedstateBeta.py $(BETADATA)
	python3.8 $< 

# Energy difference and energy levels
Energylevels.pdf: energylevels.py energies.txt fileReader.py
	python3.8 $<

Energydifference.pdf: energydifference.py energies.txt
	python3.8 $<

fileReader.py:
	cp -f $(LIBSRC)/$@ .

.PHONY: clean
clean:
	rm -f *.pdf fileReader.py
	rm -f -r __pycache__/
