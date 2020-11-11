import matplotlib.pyplot as plt

#As = [0.15, 0.33, 0.4, 0.5]
#ks = [2, 3, 4, 5]

combinations = [(2, 0.5), (3, 0.33), (4,0.4), (5,0.15)]
scale = 0.5/0.36537 #Conversion scale for time --> Time[ms]
basefilename = "QM2Clustering"

Ts = [[], [], [], []]
infs = [[], [], [], []]

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
            shakes = int(words[2])
        except:
            break
        try:
            Ts[shakes-2].append(float(words[0]) * scale)
        except:
            break
        try:
            infs[shakes-2].append(1 - float(words[1]))
        except:
            Ts[shakes-2] = Ts[shakes-2][0:-1]
            break
        line = data.readline()
    data.close()
    
#plot data
for i in range(len(Ts)):
    shakes = i+2
    T = Ts[i]
    inf = infs[i]
    plt.plot(T,inf, 'o', label='k:'+str(shakes))

# Edit fig
plt.xlabel("T [ms]")
plt.yscale("log")
plt.ylabel("1 - F")
plt.legend(loc="best")

# Save fig
plt.savefig("shakes.pdf")
plt.savefig("shakes.png")