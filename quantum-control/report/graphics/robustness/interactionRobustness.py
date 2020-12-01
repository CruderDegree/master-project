import matplotlib.pyplot as plt

Times = ["0500","0875", "1300"]
scale = 0.5/0.36537 #Conversion scale for time --> Time[ms]
basefilename = "interactionRobustness"

for T in Times:
    a = []
    inF = []
    # Open file, skip first 2 lines
    filename = basefilename + "T" + T + ".txt"
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
            a.append(float(words[0]))
        except:
            break
        try:
            inF.append(1 - float(words[1]))
        except:
            a = a[0:-1]
            break
        line = data.readline()
    data.close()
    plotlabel = "T≈" + str(float(T)/1000 * scale )[0:4] + " ms"
    plt.plot(a, inF, label=plotlabel)
    
# Edit fig
plt.xlabel("Interaction scaling, " + r"$a_I$")
plt.yscale("log")
plt.xscale("log")
plt.ylabel("Infidelity, " + r"$1 - F$")
plt.tick_params(axis='both', which='both', direction='in', bottom=True, top=True, left=True, right=True)
plt.legend(loc="best")

# Save fig
plt.savefig(basefilename + ".pdf")
plt.savefig(basefilename + ".png")