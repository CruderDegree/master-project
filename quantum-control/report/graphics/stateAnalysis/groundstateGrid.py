import matplotlib.pyplot as plt
import numpy as np

sizes = [64, 128, 256, 512, 1024]
#sizes = [64, 1024]

data = np.loadtxt("grid"+str(sizes[-1])+".csv", delimiter=',', skiprows=1) # columns: x, ground, excited
xhi = data[:, 0]
groundhi = data[:, 1]
diff = [0] * len(xhi)

for size in sizes[:-1]:
    data = np.loadtxt("grid"+str(size)+".csv", delimiter=',', skiprows=1) # columns: x, ground, excited
    
    r = sizes[-1] // size # how many times data is reused

    x = data[:, 0]
    ground = data[:, 1]
    
    k = 0
    l = 0
    for i in range(len(xhi)):
        diff[i] = groundhi[i] - ground[l]        
        k += 1
        if k==r:
            k = 0
            l += 1

    plt.plot(xhi,diff, '.', label=r"$n="+str(size)+"$")

plt.xlabel(r"$x [\mu m]$")
plt.ylabel(r"$|\psi_{1024}|^2 - |\psi_n|^2$")
plt.yscale("log")
plt.ylim([1/1000000, 0.5])
plt.xlim([-1.1, 1.1])
plt.legend(loc="best")

filename = "GroundstateGrid"
plt.savefig(filename+".pdf")
