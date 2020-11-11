import matplotlib.pyplot as plt
import numpy as np

betas = [-20, -10, 0, 10, 20]

for beta in betas:
    data = np.loadtxt("gs"+str(beta)+".csv",delimiter=',',skiprows=1)
    x = data[:, 0]
    psi = data[:, 2]
    psi /= max(psi) #normalize
    plt.plot(x,psi, label=r"$\beta=$"+str(beta))

plt.xlabel(r"x")
plt.ylabel(r"$\psi^2$")
plt.xlim([-1, 1])
plt.ylim([0, 1.05])
plt.legend(loc="best")

filename = "groundstate"
plt.savefig(filename + ".pdf")
plt.savefig(filename + ".svg")
plt.savefig(filename + ".png")
