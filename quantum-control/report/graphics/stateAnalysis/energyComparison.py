# Link to common library
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lib import jsonReader

# Load data from QEngine
datafilename = "energySpectra.json"
data = jsonReader.readJson(datafilename)

betaQ = data["beta"]
E0Q = data["E0"]
E0varQ = data["varE0"]
E1Q = data["E1"]
E1varQ = data["varE1"]
E2Q = data["E2"]
E2varQ = data["varE2"]

# Load data from Composer
import matplotlib.pyplot as plt

betaC = []
E0C = []
E0varC = []
E1C = []
E1varC = []
E2C = []
E2varC = []

datafilename = "energies.txt"
data = open(datafilename, "r")
data.readline()
# Data format:
#   0   1   2       3   4       5   6
# beta  E0  varE0   E1  varE1   E2  varE2
line = data.readline()
while line:
    ws = line.split("\t")
    betaC.append(float(ws[0]))
    E0C.append(float(ws[1]))
    E0varC.append(float(ws[2]))
    E1C.append(float(ws[3]))
    E1varC.append(float(ws[4]))
    E2C.append(float(ws[5]))
    E2varC.append(float(ws[6]))
    line = data.readline()

data.close()

# Plot all energylevels
fig1, ax1 = plt.subplots()
ax1.plot(betaC, E0C, label="E0 Composer")
ax1.plot(betaC, E1C, label="E1 Composer")
ax1.plot(betaC, E2C, label="E2 Composer")
ax1.plot(betaQ, E0Q, label="E0 QEngine")
ax1.plot(betaQ, E1Q, label="E1 QEngine")
ax1.plot(betaQ, E2Q, label="E2 QEngine")
ax1.set_xlabel(r"$\beta$ [sim. units]")
#ax1.set_xlim([-20, 20])
ax1.set_ylabel("Energy [sim. units]")
ax1.legend(loc="best")
fig1.savefig("energiesQEngineComp.pdf")
fig1.savefig("energiesQEngineComp.png")


# Plot energy differences E-Composer - E-QEngine
E0diff = [0] * len(betaQ)
E1diff = [0] * len(betaQ)
E2diff = [0] * len(betaQ)

k = len(betaQ)//len(betaC)
for i in range(len(betaC)):
    for j in range(k):
        idx = i*k + j
        E0diff[idx] = E0C[i] - E0Q[idx]
        E1diff[idx] = E1C[i] - E1Q[idx]
        E2diff[idx] = E2C[i] - E2Q[idx]

fig2, ax2 = plt.subplots()
ax2.plot([-31, 31], [0, 0], "k--", linewidth=0.5)
ax2.plot(betaQ, E0diff,".", label=r"$\Delta E_0$")
ax2.plot(betaQ, E1diff,".", label=r"$\Delta E_1$")
ax2.plot(betaQ, E2diff,".", label=r"$\Delta E_2$")
ax2.set_xlabel(r"$\beta$ [sim. units]")
ax2.set_xlim([-31, 31])
ax2.set_ylabel("Energy difference [sim. units]")
ax2.legend(loc="best")
fig2.savefig("energyDiffQEngineComp.pdf")
fig2.savefig("energyDiffQEngineComp.png")

# Plot variances of the different energies
fig3, ax3 = plt.subplots()
fig3name = "varianceComparison"
ax3.plot(betaQ, E0varC, "o-", label="E0 Composer")
ax3.plot(betaQ, E0varQ, "s-", label="E0 QEngine")
ax3.plot(betaQ, E1varC, "o-", label="E1 Composer")
ax3.plot(betaQ, E1varQ, "s-", label="E1 QEngine")
ax3.plot(betaQ, E2varC, "o-", label="E2 Composer")
ax3.plot(betaQ, E2varQ, "s-", label="E2 QEngine")
ax3.set_yscale("log")
ax3.legend(loc="best")
fig3.savefig(fig3name+".pdf")
fig3.savefig(fig3name+".png")