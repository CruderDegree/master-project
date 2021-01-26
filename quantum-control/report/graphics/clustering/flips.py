"""
We define in this script a shake to be a directional flip (a "flip")
"""
import matplotlib.pyplot as plt

def main():
    combinations = [(2, 0.5), (3, 0.33), (3,0.5), (4,0.4), (5,0.15)]
    scale = 0.5/0.36537 #Conversion scale for time --> Time[ms]

    basefilename = "QM2Clustering"

    Ts = {}
    infs = {}

    for comb in combinations:
        k, A = comb
        # Open file, skip first 2 lines
        filename = basefilename + "k" + str(k) + "A" + str(A) + ".txt"
        try:
            data = open(filename, 'r')
        except IOError:
            continue
        data.readline()
        data.readline()
        line = data.readline()
        while(line):
            words = line.split("\t")
            # Find shake in data
            shakeidx = 3
            try:
                shakes = int(words[shakeidx])
            except ValueError:
                # Undefined are assigned -1
                shakes = -1
            
            ctrltime = float(words[0])
            infidelity = 1 - float(words[1])
            
            # Append data in dict
            if shakes in Ts:
                Ts[shakes].append(ctrltime*scale)
                infs[shakes].append(infidelity)
            else:                        # Create new dict entry if first entry
                Ts[shakes] = [ctrltime*scale]
                infs[shakes] = [infidelity]
            line = data.readline()
        data.close()
    
    sortedKeys = sorted(list(Ts.keys()))       #sort keys
    shakeDiff = sortedKeys[-1]-sortedKeys[1]
    
    #plot data
    fig, ax = plt.subplots()
    cmap = plt.cm.get_cmap('cool')
    # Write plotting data into one big list
    plotTime = [] #Ts[-1]
    plotInf = [] #infs[-1]
    plotCol = [] #['k']*len(Ts[-1]) # Undefined data are black
    for key in sortedKeys[1:]:
        plotTime += Ts[key]
        plotInf += infs[key]
        plotCol += [key]*len(Ts[key])

    im = ax.scatter(plotTime, plotInf,c=plotCol, 
                    cmap=cmap, vmin=sortedKeys[1], 
                    vmax=sortedKeys[-1], alpha=0.8)
    fig.colorbar(im)
    ax.plot(Ts[-1],infs[-1],'.k',alpha=0.8, fillstyle='none',
            label='Not included', markersize=12.5)
    
    # Edit fig
    ax.set(xlabel="T [ms]", 
           yscale="log", 
           ylabel="1 - F",
           title="No. of flips")
    
    ax.legend(loc="best")
    # Save fig
    fig.savefig("flips.pdf")
    fig.savefig("flips.png")
    
    return 0

if __name__ == "__main__":
    main()
