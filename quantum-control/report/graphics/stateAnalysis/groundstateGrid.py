import matplotlib.pyplot as plt
import numpy as np

sizes = [64, 128, 256, 512, 1024]
#sizes = [64, 1024]

data = np.loadtxt("grid"+str(sizes[-1])+".csv", delimiter=',', skiprows=1) # columns: x, ground, excited
xhi = data[:, 0]
#print("Length of highres data:", len(xhi))
groundhi = data[:, 1]

#diff = [0] * len(xhi)

for size in sizes[:-1]:
    data = np.loadtxt("grid"+str(size)+".csv", delimiter=',', skiprows=1) # columns: x, ground, excited
    
    r = sizes[-1] // size # how many times data is reused
    
    x = data[:, 0]
    ground = data[:, 1]
    #print("test ground is not 0", ground[0])
    #print("ground type:", type(ground))
    #print("Resolution of", size, ":", len(x))    
    
    psi = groundhi.copy()
    for i in range(len(ground)):
        for j in range(r):
            psi[r*i + j] = ground[i]
    #print("Psi type:", type(psi))
    #print("Test that psi[0] is not 0", psi[0])
    #print("psi",psi)
    diff = groundhi - psi
    
    #print("diff", diff)
    plt.plot(xhi,diff, '.', label=r"$n="+str(size)+"$")

plt.xlabel(r"$x [\mu m]$")
plt.ylabel(r"$|\psi_{1024}|^2 - |\psi_n|^2$")
plt.yscale("log")
plt.ylim([1e-8, 0.5])
plt.xlim([-1.1, 1.1])
plt.legend(loc="best")

filename = "GroundstateGrid"
plt.savefig(filename+".pdf")
