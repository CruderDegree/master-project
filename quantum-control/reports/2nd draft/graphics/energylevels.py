import matplotlib.pyplot as plt
from fileReader import fileReader
from math import sqrt


beta = []
E0 = []
varE0 = []
E1 = []
varE1 = []

beta, E0, varE0, E1, varE1 = fileReader("energylevels.txt", beta, E0, varE0, E1, varE1, skiplines=2)

errE0 = [0] * len(varE0)
errE1 = [0] * len(varE1)

E0Upper = [0] * len(varE0)
E0Lower = [0] * len(varE0)

E1Upper = [0] * len(varE0)
E1Lower = [0] * len(varE0)



for i in range(len(varE0)):
    errE0[i] = sqrt(varE0[i])
    errE1[i] = sqrt(varE1[i])
    
    E0Upper[i] = E0[i] + errE0[i]
    E0Lower[i] = E0[i] - errE0[i]

    E1Upper[i] = E1[i] + errE1[i]
    E1Lower[i] = E1[i] - errE1[i]

plt.fill_between(beta,E0Upper,E0Lower, alpha=0.25, color="b")
plt.fill_between(beta,E1Upper,E1Lower, alpha=0.25, color="r")
plt.plot(beta,E0,color="b",label="E0")
plt.plot(beta,E1,color="r",label="E1")
plt.xlabel(r"$\beta$")
plt.ylabel("Energy")
plt.legend(loc="best")

filename = "energylevels"
plt.savefig(filename+".pdf")
plt.savefig(filename+".png")
plt.savefig(filename+".svg")
