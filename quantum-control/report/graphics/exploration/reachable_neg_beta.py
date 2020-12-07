import matplotlib.pyplot as plt
from fileReader import fileReader
# Other times: 0.8, 1.5, 2,
timescales = [0.9,1,1.25]
filename = "reachable_neg_beta"

for T in timescales:
    beta = []
    F = []
    beta, F = fileReader(filename+str(T)+".txt", beta, F, skiplines=2)

    inF = [1] * len(F)
    for i in range(len(F)):
        inF[i] -= F[i]

    #minb = beta[0]
    minb = -15
    maxb = -5
    #plt.plot(beta,inF, 'k-', linewidth=0.5)
    name = "T = "+str(T)
    plt.plot(beta,inF, '-', linewidth=1, label=name)

plt.plot([minb, maxb], [1-0.99, 1-0.99], 'r--', linewidth=0.75)
plt.xlabel("β")
plt.ylabel("Infidelety 1 - F")
plt.xlim(minb, maxb)
plt.legend(loc="best")
plt.yscale("log") # Log scale
#plt.xscale("log")

plt.savefig(filename+".pdf")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")

