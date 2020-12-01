"""
Reads QEngine json and plots unoptimized and optimized control function
"""
import matplotlib.pyplot as plt

# Link to common library
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lib import jsonReader

# Read QEngine data
datafilename = "gpe-tester.json"
data = jsonReader.readJson(datafilename)

duration = data["duration"]
t = data["t"][0]
uGrape = data["u_grape"][0]
uUnopt = data["u_unopt"][0]
print("control duration", duration)
print("Length of t:",len(t))
print("Length of uGrape:",len(uGrape))
print("Length of uUnopt:",len(uUnopt))

plt.plot(t, uUnopt, "b-", label="Inital control")
plt.plot(t, uGrape, "r-", label="Grape optimized control")
plt.legend(loc="best")
plt.xlim([0, duration])
plt.xlabel("Time [ms]")
plt.ylabel(r"Control displacement [$\mu$m]")
plt.savefig("testPlotControls.pdf")