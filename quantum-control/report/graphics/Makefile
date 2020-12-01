ComposerScreens = grape_highlight.png grape_highlight.svg grape.png simulation.png system.png
ExplorationFigs = nonOptBeta.pdf QSL.pdf betaNonOptFidelityBeta7.png betaNonOptFidelityBeta12.png
StateAnalysisFigs = GroundstateGrid.pdf GroundstateBeta.pdf ExcitedstateGrid.pdf ExcitedstateBeta.pdf Energylevels.pdf Energydifference.pdf
ClusteringFigs = QM2Clustering.pdf 
RobustnessFigs = interactionRobustness.pdf robustness.pdf



all: $(StateAnalysisFigs) $(ComposerScreens)

$(StateAnalysisFigs): stateAnalysis/*.py stateAnalysis/*.csv stateAnalysis/*.txt
	(cd stateAnalysis; make all; cp -f $(StateAnalysisFigs) ..)

$(ComposerScreens):
	(cd composerScreens; cp -f $(ComposerScreens) ..)

$(ExplorationFigs): exploration/*.py exploration/*.txt
	(cd exploration; make all; cp -f $@ ..)

.PHONY: clean
clean:
	rm -f $(StateAnalysisFigs)
	(cd stateAnalysis; make clean) # stateanalysis folder
