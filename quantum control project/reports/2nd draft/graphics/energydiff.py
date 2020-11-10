import matplotlib.pyplot as plt
from fileReader import fileReader
from math import sqrt


beta = []
E0 = []
E1 = []
E2 = []
varE2 = []

beta, E0, E1, E2, varE2 = fileReader("energysplitting.txt", beta, E0, E1, E2, varE2, skiplines=2)



errE2 = [0] * len(varE2)
E01 = [0] * len(varE2)
E12 = [0] * len(varE2)
E12Upper = [0] * len(varE2)
E12Lower = [0] * len(varE2)

for i in range(len(varE2)):
    E01[i] = E1[i] - E0[i]
    E12[i] = E2[i] - E1[i]
    errE2[i] = sqrt(varE2[i])
    E12Upper[i] = E12[i] + errE2[i]
    E12Lower[i] = E12[i] - errE2[i]

plt.fill_between(beta,E12Upper,E12Lower, alpha=0.25,color="r")
plt.plot(beta,E01,"b",label=r"$E_1 - E_0$")
plt.plot(beta,E12,"r",label=r"$E_2 - E_1$")
plt.xlabel(r"$\beta$")
plt.ylabel(r"$\Delta E$")
plt.legend(loc="best")

filename = "energydiff"
plt.savefig(filename+".pdf")
plt.savefig(filename+".png")
plt.savefig(filename+".svg")
