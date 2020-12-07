"""
TODO
"""

# Link to common library
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lib import jsonReader

import matplotlib.pyplot as plt

## Plot data from Composer
ComposerData = open("nonOptBeta-comparison.txt","r")
ComposerData.readline()
line = ComposerData.readline()
bC = []
FC = []
while line:
    ws = line.split("\t")
    bC.append(float(ws[0]))
    FC.append(float(ws[1]))
    line = ComposerData.readline()

plt.plot(bC, FC, "bs-", label="Composer")

# PLot data from QEngine

datafilename = "nonOptSolutions.json"

data = jsonReader.readJson(datafilename)

t = data["t"][0]
duration = data["duration"]
i = 0
while(t[i] < duration):
    i += 1

bQ = []
FQ = []

for key in data.keys():
    if len(key) > 14 and key[:14] == "fidelity_unopt":
        bQ.append(key[14:])
bQ.sort(key=lambda x: float(x))
for beta in bQ:    
    key = "fidelity_unopt" + beta
    FQ.append(float(data[key][i]))

for i in range(len(bQ)):
    bQ[i] = float(bQ[i])

plt.plot(bQ, FQ, "r-", label="QEngine")
plt.ylabel("Fidelity at t=T")
plt.xlabel(r"$\beta$")
plt.legend(loc="best")
plt.savefig("comparison.pdf")
plt.savefig("comparison.png")