import matplotlib.pyplot as plt
import numpy as np
import json

names = ["altcos-end-both-4","altcos-mid-cos-6", "both-mid-none-3", "both-none-both-3","cos-mid-cos-3", "cos-none-none-4"]
colors = [""]
medians = []
upper_quarts = []
lower_quarts = []
bests = []
t = np.linspace(0, 1, 501)
fig, ax = plt.subplots()

for i in range(len(names)):
    name = names[i]
    f = open("./seeding_strats_results/seeding-strategy-"+name+".json", "r")
    data = json.load(f)
    f.close()
    lower_quarts.append([])
    medians.append([])
    upper_quarts.append([])
    bests.append([])
    
    for duration in data["durations"]:
        # Note quantiles for later plotting
        lower, median, upper, best = np.quantile(data["fidelity_grape_"+"{0:g}".format(duration)], [0.25, 0.50, 0.75, 1])
        lower_quarts[i].append(1 - lower)
        medians[i].append(1 - median)
        upper_quarts[i].append(1 - upper)
        bests[i].append(1 - best)

        # Plot unoptimized controls    
        for j in range(int(data["noise_iter"])):
            u = data["ctrl_"+"{0:g}".format(duration)+"_unopt"]["data"][j][0]
            ax.plot(t, u, alpha=0.25)
        ax.set_title(name + " seeds")
        ax.set_xlabel("t/T")
        ax.set_ylabel("u(t) [ms]")
        fig.savefig("./seeding_strats_qengine_controls/"+name+"seed"+str(duration)+".pdf")
        fig.savefig("./seeding_strats_qengine_controls/"+name+"seed"+str(duration)+".png")
        ax.clear()

# Plot fidelity performances
# Plot quantiles
for i in range(len(names)):
    ax.fill_between(list(data["durations"]), lower_quarts[i], upper_quarts[i], alpha=0.2, color="C"+str(i))
    ax.plot(list(data["durations"]),medians[i],"-", color="C"+str(i), label=names[i])
    ax.plot(list(data["durations"]), bests[i], '-x', color="C"+str(i))
ax.set_xlabel("Control duration [ms]")
ax.set_xticks([0.5, 0.75, 1, 1.25, 1.5])
ax.set_ylabel(r"Infidelity, $1 - F$")
ax.set_yscale("log")
ax.legend(loc="best")
fig.savefig("./seeding_strats_results/quantiles.pdf")
fig.savefig("./seeding_strats_results/quantiles.png")
ax.clear
# Plot best