import matplotlib.pyplot as plt

#As = [0.15, 0.33, 0.4, 0.5]
#ks = [2, 3, 4, 5]
Times = ["0500","0875", "1300"]
scale = 0.5/0.36537 #Conversion scale for time --> Time[ms]
basefilename = "robustness"

for T in Times:
    a = []
    inF = []
    # Open file, skip first 2 lines
    filename = basefilename + "T" + T + "Pot" + ".txt"
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
plt.xlabel("Potential scaling, " + r"$a_V$")
plt.yscale("log")
plt.xlim([0.9, 1.1])
plt.ylabel("Infidelity, " + r"$1 - F$")
plt.tick_params(axis='both', which='both', direction='in', bottom=True, top=True, left=True, right=True)
plt.legend(loc="best")

# Save fig
plt.savefig(basefilename + ".pdf")
plt.savefig(basefilename + ".png")