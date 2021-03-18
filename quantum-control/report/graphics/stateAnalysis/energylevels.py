import matplotlib.pyplot as plt
from fileReader import fileReader
from math import sqrt

linestyle_dict = {"A" : "-", "B" : "--"}

for N in ["A", "B"]:

    beta = []
    E0 = []
    varE0 = []
    E1 = []
    varE1 = []
    E2 = []
    varE2 = []

    beta, E0, varE0, E1, varE1, E2, varE2 = fileReader("energies"+N+"1.txt", beta, E0, varE0, E1, varE1, E2, varE2, skiplines=1)

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
    plt.plot(beta,E0,"b"+linestyle_dict[N],label=r"$E_{"+N+"0}$")
    plt.plot(beta,E1,"r"+linestyle_dict[N],label=r"$E_{"+N+"1}$")
    plt.plot(beta,E2,"g"+linestyle_dict[N],label=r"$E_{"+N+"2}$")
    
plt.xlabel(r"$\beta$")
plt.ylabel(r"Energy [Sim.]")
plt.ylim([-40, 60])
plt.xlim([-30, 30])
plt.legend(loc="best", ncol=2)

filename = "Energylevels"
plt.savefig(filename+".pdf")
plt.savefig(filename+".png")