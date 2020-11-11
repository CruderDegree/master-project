import matplotlib.pyplot as plt

beta = [-5,-3,0,0.5,1,5,10,11,13,15,17.5,19,25]
t = [1,0.83,0.75,0.9,0.8,0.9,1,1,1.1,1.35,1.35,1.36,1.49]

minb = -5
maxb = 25
plt.plot(beta,t, 'b.')
plt.plot(beta,t, 'k-', linewidth=0.5)
#plt.plot([2*minb, 2*maxb], [0.75, 0.75], 'r--')
plt.xlim(minb - 2, maxb + 2)
plt.xlabel("β")
plt.ylabel("Quantum speed limit")
filename = "QSL"
plt.savefig(filename+".pdf")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")

