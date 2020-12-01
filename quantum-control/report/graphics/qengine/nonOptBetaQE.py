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

datafilename = "nonOptSolutions.json"

data = jsonReader.readJson(datafilename)

t = data["t"][0]
F = data["fidelity_unopt"]

# Find fidelity at t=T
duration = data["duration"]
i = 0
while(t[i] < duration):
    i += 1
print("Fidelity reached:", F[i])
