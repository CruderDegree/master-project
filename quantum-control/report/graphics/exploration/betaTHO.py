import matplotlib.pyplot as plt
from fileReader import fileReader

Ts = [1, 2.5, 7.5]
basename = "betaTHO"
colors = ["blue", "green", "red"]
markers = ["o", "s", "v"]
assert(len(Ts) == len(colors) == len(markers))
N = len(Ts)
betamin = 100
betamax = -100

for n in range(N):
    T = Ts[n]
    beta = []
    F = []
    fileReader(basename + str(T) + ".txt", beta, F, skiplines=1)
    #plt.plot(beta,F,color=colors[n],linewidth=0.1)
    plt.plot(beta,F,color=colors[n], marker=markers[n], label="T = "+str(T),
             linewidth=0.75)
    if beta[0] < betamin:
        betamin = beta[0]
    if beta[-1] > betamax:
        betamax = beta[-1]


plt.xlim(betamin - 2, betamax + 2)
plt.xlabel("β")
plt.ylabel("Maximum achievable fidelity")
plt.legend(loc='upper left')

#Save fig
plt.savefig(basename + ".pdf")
plt.savefig(basename + ".png")
#plt.show()
