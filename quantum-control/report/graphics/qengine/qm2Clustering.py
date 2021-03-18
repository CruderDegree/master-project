"""
Do a clustering solution similar to that in QM2 paper for the controls found.
"""
# Link to common library
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lib import jsonReader
import matplotlib.pyplot as plt
import numpy as np
import math, time
from sklearn.cluster import DBSCAN

def main():
    then = time.time()
    #files = ["composerReplication-redo.json"] # Single file
    files = ["composerReplication-redo.json", "composerReplication-2-redo.json", "composerReplication-3.json", "composerReplication-4.json"] # All files
    timescale = 0.5/0.36537
    minimum_fidelity = 0.7
    timesteps = 501
    ncontrols = 0 # Number of clustered funcs
    #Cluster settings
    eps = 0.05
    min_samples = 10

    cks = []
    Ts = []
    Infs = []
    ctrls = []

    for datafile in files:
        data = jsonReader.readJson(datafile)

        ## Read durations
        durations = data["durations"]
        iterations = int(data["noise_iter"])
        optimizers = ["grape", "group", "dgroup"]
        
        for T in durations:
            for optimizer in optimizers:
                for i in range(iterations):
                    try:
                        fidelity = data["fidelity_"+optimizer+"_"+str(T)][i]
                    except KeyError:
                        if "fidelity_"+optimizer+"_"+str(int(T)) in data.keys():
                            fidelity = data["fidelity_"+optimizer+"_"+str(int(T))][i]
                        else:
                            #print("KeyError:", datafile, optimizer, T)
                            continue
                    if fidelity > minimum_fidelity:
                        ncontrols += 1
                        try:
                            x = data["x_expect_"+optimizer+"_"+str(T)][0 + timesteps*i:timesteps + timesteps*i]
                            u = data["ctrl_"+str(T)+"_"+optimizer]["data"][i][0]
                        except KeyError:
                            x = data["x_expect_"+optimizer+"_"+str(int(T))][0 + timesteps*i:timesteps + timesteps*i]
                            u = data["ctrl_"+str(int(T))+"_"+optimizer]["data"][i][0]
                        ck = calc_ck(x, u, T)
                        cks += ck
                        ctrls.append(np.array(u)-np.array(x))
                        Ts.append(T*timescale)
                        Infs.append(1-fidelity)

    cks = np.reshape(cks, (ncontrols, len(ck)))
    ctrls = np.reshape(ctrls, (ncontrols, timesteps))

    
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(cks)
    labels = db.labels_
    nclusters = len(set(labels)) - (1 if -1 in labels else 0) # Count clusters - noise
    n_noise = list(labels).count(-1)

    print("Number of analyzed controls:", ncontrols)
    print("Estimated number of clusters:", nclusters)
    print("Estimated number of noise points:", n_noise)

    fig, ax = plt.subplots()
    colorDict = {-1: [0,0,0], 0: [1,0,0], 1: [x/255.0 for x in [0,120,255]], 2: [x/255.0 for x in [0,200,0]], 3: np.array([178,102,255])/255.0, 4:[0.5,0.5,0.5]}
    while len(colorDict) < nclusters + 1:
        colorDict[len(colorDict) - 1] = np.random.rand(3)
    ax.scatter(Ts, Infs, s=10.0, c=[colorDict[label] for label in labels])
    ax.set( xlabel="Control Duration [ms]",
            ylabel=r"$1-F$",
            yscale="log")
    for k in set(labels):
        if k == -1:
            label = "Unclassified"
        else:
            label = "Cluster " + str(k)
        ax.plot([0.1278*timescale], [1-0.99432], '.', color=colorDict[k], label=label)
    ax.legend(loc='lower left')

    ax.set_yticks([1, 1-0.9, 1-0.99])
    ax.set_ylim([1-0.998,1])
    #ax.set_yticklabels([r"$10^{0}$", r"$10^{-1}$", r"$10^{-2}$"])

    filename = "QEclustering-classification"
    fig.savefig(filename+".pdf")
    fig.savefig(filename+".png")

    # Feature plot ck(k) for each cluster
    fig, ax = plt.subplots()

    for i in range(nclusters):
        where = np.where(np.array(labels) == i)
        mean = np.mean(cks[where], axis=0)
        std = np.std(cks[where], axis=0)
        #ax.plot([k for k in range(len(ck))], mean, '--', color=colorDict[i]) # plot line
        ax.errorbar([k for k in range(len(ck))], mean, yerr=std,capsize=5, color=colorDict[i],label="Cluster "+str(i), linestyle='--')

    ax.set_xticks(list(range(len(ck))))
    ax.set( xlabel=r"$k$",
            ylabel=r"$c_k$")
    ax.legend(loc="best")

    filename = "QEclustering-features"
    fig.savefig(filename+".pdf")
    fig.savefig(filename+".png")

    # Cluster mean u-x for each cluster
    fig, ax = plt.subplots()

    t = np.linspace(0,1,timesteps)
    for i in range(nclusters):
        where = np.where(np.array(labels) == i)
        mean = np.mean(ctrls[where], axis=0)
        ax.plot(t, mean, '-',color=colorDict[i])
    ax.set( xlabel=r"$t/T$",
            ylabel=r"$u-<x> [\mu m]$")
    ax.set_ylim([-1, 1])

    ax.plot([0,1],[0,0],'k-',linewidth=0.5)

    filename = "QEclustering-means"
    fig.savefig(filename+".pdf")
    fig.savefig(filename+".png")
    now = time.time()
    print("Time elapsed:",now-then, "s")
    return 0

def calc_ck(x: list, u: list, T: float, nsteps=501, ks=5) -> list:
    cks = [0] * (ks + 1)
    dt = T/nsteps
    for k in range( ks ):
        res = 0
        t = 0
        for n in range(nsteps):
            t += dt
            res += (u[n]-x[n])*math.cos(math.pi * k * t / T) * dt
        cks[k] = res/T
    return cks


if __name__ == "__main__":
    main()
