"""
Plot infidelity of all optimized controls as a function of control duration
"""
# Link to common library
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lib import jsonReader

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Plot highest fidelities from Composer Clustering
CompData = open("clustering_best.txt","r")
scale = 0.5/0.36537 #Conversion scale for time --> Time[ms]
T = []
inF = []
CompData.readline()
line = CompData.readline()
while(line):
    words = line.split("\t")
    try:
        T.append(float(words[0]) * scale)
    except:
        break
    try:
        inF.append(1 - float(words[1]))
    except:
        T = T[0:-1]
        break
    line = CompData.readline()
CompData.close()
plotlabel = "Composer best"
ax.plot(T, inF,".-", color="orangered", label=plotlabel)

maxT = 0.8125
minInf = {} # Note best fidelities and times
times = []

#files = ["composerReplication-2-redo.json"] # Single files
files = ["composerReplication-redo.json", "composerReplication-2-redo.json", "composerReplication-3.json", "composerReplication-4.json"] # All files
for datafile in files:
    data = jsonReader.readJson(datafile)

    ## Read durations
    durations = data["durations"]
    iterations = int(data["noise_iter"])

    optimizers = ["grape_", "group_", "dgroup_"]
    labelDict = {"grape_":"GRAPE", "group_":"GROUP", "dgroup_":"dGROUP"}
    plotDict = {"grape_":"orange", "group_":"blue", "dgroup_":"green"}

    for optimizer in optimizers:
        for duration in durations:
            if duration >= maxT:
                continue
            ## Load fidelities
            try:
                fidelities = data["fidelity_"+optimizer+str(duration)]
            except KeyError:
                if "fidelity_"+optimizer+str(int(duration)) in data.keys():
                    fidelities = data["fidelity_"+optimizer+str(int(duration))]
                else:
                    continue
                            
            if duration not in times:
                times.append(duration)
                minInf[duration] = 1

            # Calc 1 - F
            infidelities = [1] * iterations
            for i in range(iterations):
                infidelities[i] -= fidelities[i]
                if infidelities[i] < minInf[duration]:
                    minInf[duration] = infidelities[i]

            ax.plot([duration*scale]*iterations, infidelities, '.', alpha=0.4, color=plotDict[optimizer])
    
# Plot best for QEngine
times.sort()
ax.plot([scale * t for t in times], [minInf[time] for time in times], '.-', color="purple", label="QEngine best")


ax.set_yscale("log")
ax.set_xlabel("Control duration [ms]")
ax.set_ylabel("1 - F")
ax.legend(loc="best")

fig.savefig("noiseDemoInf.pdf")
fig.savefig("noiseDemoInf.png")