import matplotlib.pyplot as plt
from fileReader import fileReader

# list with (A,k) tubles
paramlist = [(1,1), (1,2), (1,3), (0.5,1), (0.5,2), (0.5,3), (0.33, 1), (2,1), (1.5, 1), (1.5, 2)]
paramlist = sorted(paramlist)
filename = "clustering"

for i in range(len(paramlist)):
    if paramlist[i][1] != 1:
        continue
    T = []
    F = []
    A, k = paramlist[i]
    T, F = fileReader(filename+"A"+str(A)+"k"+str(k)+".txt", T, F, skiplines=2)
    inF = [1] * len(F)
    for i in range(len(F)):
        inF[i] -= F[i]
    name = r"$A:"+str(A)+", k:"+str(k)+"$"
    plt.plot(T,inF, label=name)

plt.xlabel(r"T")
plt.ylabel(r"$1-F$")
plt.yscale("log")
plt.legend(loc="best")
plt.xlim([0.7, 1.2])
filename += "k1"
plt.savefig(filename + ".pdf")
plt.savefig(filename + ".svg")
plt.savefig(filename + ".png")
