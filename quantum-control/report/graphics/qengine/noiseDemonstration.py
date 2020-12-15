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

## Read durations
durations = data["durations"]
iterations = 10

for duration in durations:
    try:
        fidelities = data["fidelity_grape_"+str(duration)]
    except KeyError:
        try:
            fidelities = data["fidelity_grape_"+str(round(duration, 2))]
        except KeyError:
            fidelities = data["fidelity_grape_"+str(int(duration))]
    
    infidelities = [1] * iterations
    for i in range(iterations):
        infidelities[i] -= fidelities[i]
    
    ax.plot([duration]*iterations, infidelities, 'b.')

ax.set_yscale("log")
ax.set_xlabel("Control time [ms]")
ax.set_ylabel("1 - F")

fig.savefig("noiseDemoInf.pdf")
fig.savefig("noiseDemoInf.png")