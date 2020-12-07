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

E0Upper = [0] * len(varE0)
E0Lower = [0] * len(varE0)
E1Upper = [0] * len(varE0)
E1Lower = [0] * len(varE0)
E2Upper = [0] * len(varE0)
E2Lower = [0] * len(varE0)

for i in range(len(varE0)):
    E0Upper[i] = E0[i] + sqrt(varE0[i])
    E0Lower[i] = E0[i] - sqrt(varE0[i])

    E1Upper[i] = E1[i] + sqrt(varE1[i])
    E1Lower[i] = E1[i] - sqrt(varE1[i])

    E2Upper[i] = E2[i] + sqrt(varE2[i])
    E2Lower[i] = E2[i] - sqrt(varE2[i])


plt.fill_between(beta,E0Upper,E0Lower, alpha=0.25, color="b")
plt.fill_between(beta,E1Upper,E1Lower, alpha=0.25, color="r")
plt.fill_between(beta,E2Upper,E2Lower, alpha=0.25, color="g")
plt.plot(beta,E0,color="b",label=r"$E_0$")
plt.plot(beta,E1,color="r",label=r"$E_1$")
plt.plot(beta,E2,color="g",label=r"$E_2$")
plt.xlabel(r"$\beta$")
plt.ylabel(r"Energy")
plt.legend(loc="best")

filename = "Energylevels"
plt.savefig(filename+".pdf")
plt.savefig(filename+".png")