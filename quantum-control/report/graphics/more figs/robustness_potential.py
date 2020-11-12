import matplotlib.pyplot as plt
from fileReader import fileReader

alfa = []
F = []
alfa, F = fileReader("robustness_potential.txt", alfa, F, skiplines=2)

inF = [1] * len(F)
for i in range(len(F)):
    inF[i] -= F[i]

minb = alfa[0]
maxb = alfa[-1]
plt.plot(alfa,inF, 'r-')
plt.xlabel("Potential scaling a")
plt.ylabel("Infidelity")
plt.xlim(minb, maxb)
plt.yscale("log") # Log scale

filename = "robustness_potential"
plt.savefig(filename+".pdf")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")

