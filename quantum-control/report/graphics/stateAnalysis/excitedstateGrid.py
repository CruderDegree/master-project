import matplotlib.pyplot as plt
import numpy as np

sizes = [64, 128, 256, 512, 1024]

data = np.loadtxt("grid"+str(sizes[-1])+".csv", delimiter=',', skiprows=1) # columns: x, ground, excited
xhi = data[:, 0]
excitedhi = data[:, 2]
diff = [0] * len(xhi)

for size in sizes[:-1]:
    data = np.loadtxt("grid"+str(size)+".csv", delimiter=',', skiprows=1) # columns: x, ground, excited
    
    r = sizes[-1] // size # how many times data is reused

    x = data[:, 0]
    excited = data[:, 2]
    
    psi = excitedhi.copy()
    for i in range(len(excited)):
        for j in range(r):
            psi[r*i + j] = excited[i]
    print("Psi type:", type(psi))
    print("Test that psi[0] is not 0", psi[0])
    print("psi",psi)
    diff = excitedhi - psi
    

    plt.plot(xhi,diff, '.', label=r"$n="+str(size)+"$")

plt.xlabel(r"$x [\mu m]$")
plt.ylabel(r"$|\psi_{1024}|^2 - |\psi_n|^2$")
plt.yscale("log")
plt.ylim([1e-8, 0.5])
plt.xlim([-1.1, 1.1])
plt.legend(loc="best")

filename = "ExcitedstateGrid"
plt.savefig(filename+".pdf")
