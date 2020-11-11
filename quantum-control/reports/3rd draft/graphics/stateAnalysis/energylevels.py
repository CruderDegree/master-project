import matplotlib.pyplot as plt
from fileReader import fileReader
from math import sqrt


beta = []
E0 = []
varE0 = []
E1 = []
varE1 = []
E2 = []
varE2 = []

beta, E0, varE0, E1, varE1, E2, varE2 = fileReader("energies.txt", beta, E0, varE0, E1, varE1, E2, varE2, skiplines=1)

E01 = E1.copy()
E12 = E2.copy()
E01Upper = [0] * len(varE0)
E01Lower = [0] * len(varE0)
E12Upper = [0] * len(varE0)
E12Lower = [0] * len(varE0)

for i in range(len(varE0)):
    E01[i] -= E0[i]
    E12[i] -= E1[i]

    E01err = sqrt(varE0[i] + varE1[i])
    E12err = sqrt(varE1[i] + varE2[i])
    
    E01Upper[i] = E01[i] + E01err
    E01Lower[i] = E01[i] - E01err

    E12Upper[i] = E12[i] + E12err
    E12Lower[i] = E12[i] - E12err

plt.fill_between(beta,E01Upper,E01Lower, alpha=0.25, color="b")
plt.fill_between(beta,E12Upper,E12Lower, alpha=0.25, color="r")
plt.plot(beta,E01,color="b",label=r"$E_1 - E_0$")
plt.plot(beta,E12,color="r",label=r"$E_2 - E_1$")
plt.xlabel(r"$\beta$")
plt.ylabel(r"$\Delta E$")
plt.legend(loc="best")

filename = "Energydifference"
plt.savefig(filename+".pdf")
