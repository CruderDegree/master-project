import matplotlib.pyplot as plt
from fileReader import fileReader

beta = []
F = []
beta, F = fileReader("robustness_beta.txt", beta, F, skiplines=2)

inF = [1] * len(F)
for i in range(len(F)):
    inF[i] -= F[i]

minb = beta[0]
maxb = beta[-1]
#plt.plot(beta,inF, 'k-', linewidth=0.5)
plt.plot(beta,inF, 'r-')
plt.xlabel("Interaction scaling a")
plt.ylabel("Infidelity")
plt.xlim(minb, maxb)
plt.yscale("log") # Log scale
plt.xscale("log")

filename = "robustness_beta"
plt.savefig(filename+".pdf")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")

