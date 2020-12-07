import matplotlib.pyplot as plt

#As = [0.15, 0.33, 0.4, 0.5]
#ks = [2, 3, 4, 5]

combinations = [(2, 0.5), (3, 0.33), (4,0.4), (5,0.15)]
scale = 0.5/0.36537 #Conversion scale for time --> Time[ms]
basefilename = "QM2Clustering"

for comb in combinations:
    k, A = comb
    T = []
    inF = []
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
        try:
            T.append(float(words[0]) * scale)
        except:
            break
        try:
            inF.append(1 - float(words[1]))
        except:
            T = T[0:-1]
            break
        line = data.readline()
    data.close()
    plotlabel = r"$k:" + str(k) + ", A:" + str(A) +"$"
    plt.plot(T, inF,".-", label=plotlabel)
    
# Edit fig
plt.xlabel("T [ms]")
plt.yscale("log")
plt.ylabel("1 - F")
plt.legend(loc="best")

# Save fig
plt.savefig(basefilename + ".pdf")
plt.savefig(basefilename + ".png")