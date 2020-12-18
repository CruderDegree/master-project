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

datafilename = "seedNoiseDemo.json"

data = jsonReader.readJson(datafilename)

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
plotlabel = "Composer"
ax.plot(T, inF,".-", color="orangered", label=plotlabel)

## Read durations
durations = data["durations"]
iterations = int(data["noise_iter"])

optimizers = ["grape_", "group_", "dgroup_"]
labelDict = {"grape_":"GRAPE", "group_":"GROUP", "dgroup_":"dGROUP"}
plotDict = {"grape_":"orange", "group_":"blue", "dgroup_":"green"}

for optimizer in optimizers:
    maxFs = []
    for duration in durations:
        ## Load fidelities
        try:
            fidelities = data["fidelity_"+optimizer+str(duration)]
        except KeyError:
            try:
                fidelities = data["fidelity_"+optimizer+str(round(duration, 2))]
            except KeyError:
                fidelities = data["fidelity_"+optimizer+str(int(duration))]
        
        # Calc 1 - F
        infidelities = [1] * iterations
        maxF = fidelities[0]
        for i in range(iterations):
            infidelities[i] -= fidelities[i]
            if fidelities[i] > maxF:
                maxF = fidelities[i]
        maxFs.append(1-maxF)
        ax.plot([duration]*iterations, infidelities, '.', alpha=0.4, color=plotDict[optimizer])
        
    ax.plot(durations, maxFs, '.', color=plotDict[optimizer], label=labelDict[optimizer])

ax.set_yscale("log")
ax.set_xlabel("Control time [ms]")
ax.set_ylabel("1 - F")
ax.legend(loc="best")

fig.savefig("noiseDemoInf.pdf")
fig.savefig("noiseDemoInf.png")