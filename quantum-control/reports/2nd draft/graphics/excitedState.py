import matplotlib.pyplot as plt
import numpy as np

# excluded are beta = 10,30 and +- 5
betas = [-10, 0, 10]
colordict = {-10:"orange", 0:"green", 10:"red"}
#betas = sorted(betas,reverse=True)

for beta in betas:
    data = np.loadtxt("excs"+str(beta)+".csv",delimiter=',',skiprows=1)
    x = data[:, 0]
    psi = data[:, 1]
    psi /= max(psi)
    #if beta == betas[0]: #plot potential once
    #    V = data[:,1]
    #    plt.plot(x,V, "--k", label="V(x)")    
    plt.plot(x,psi,color=colordict[beta], label=r"$\beta=$"+str(beta))

plt.xlabel(r"x")
plt.ylabel(r"$\psi^2$")
plt.xlim([-1, 1])
plt.ylim([0, 1.05])
plt.legend(loc="best")

filename = "excitedstate"
plt.savefig(filename + ".pdf")
plt.savefig(filename + ".svg")
plt.savefig(filename + ".png")
