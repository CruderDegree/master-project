StateAnalysisFigs = GroundstateGrid.pdf GroundstateBeta.pdf ExcitedstateGrid.pdf ExcitedstateBeta.pdf Energylevels.pdf Energydifference.pdf


all: $(StateAnalysisFigs)

$(StateAnalysisFigs): stateAnalysis/*.py stateAnalysis/*.csv stateAnalysis/*.txt
	(cd stateAnalysis; make all; cp -f $(StateAnalysisFigs) ..)


.PHONY: clean
clean:
	rm -f $(StateAnalysisFigs)
	(cd stateAnalysis; make clean) # stateanalysis folder
