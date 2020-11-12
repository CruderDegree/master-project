import matplotlib.pyplot as plt
from fileReader import fileReader

# list with (A,k) tubles
# Excluded data (1.5, 1)(1.5,2)(2,1)
paramlist = [(1,1), (1,2), (1,3), (0.5,1), (0.5,2), (0.5,3), (0.33, 1)]
paramlist = sorted(paramlist, key = lambda x: x[1])
filename = "clustering"
scale = 0.5/0.36537
for i in range(len(paramlist)):
    T = []
    F = []
    A, k = paramlist[i]
    T, F = fileReader(filename+"A"+str(A)+"k"+str(k)+".txt", T, F, skiplines=2)
    inF = [1] * len(F)
    for i in range(len(F)):
        T[i] *= scale
        inF[i] -= F[i]
    name = r"$k:"+str(k)+", A:"+str(A)+"$"
    plt.plot(T,inF, label=name)

plt.xlabel(r"T [ms]")
plt.ylabel(r"$1-F$")
plt.yscale("log")
plt.legend(loc="best")

plt.xlim([0.7*scale, 1.1*scale])

plt.savefig(filename + ".pdf")
plt.savefig(filename + ".svg")
plt.savefig(filename + ".png")
