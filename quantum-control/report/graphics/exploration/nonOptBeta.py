"""
REsulting fidelity of variying beta in a non-optimized solution in a quatic potential
"""
import matplotlib.pyplot as plt

filename = "nonOptBeta"

beta = []
F = []
data = open(filename+".txt", 'r')
data.readline()
line = data.readline()
while(line):
    ws = line.split('\t')
    beta.append(float(ws[0]))
    F.append(float(ws[1]))
    line = data.readline()
data.close()

plt.plot(beta,F, 's-')
plt.xlabel(r"Self interaction strength $\beta$ [sim]")
plt.ylabel("Fidelity at t=T")

plt.savefig(filename+".pdf")