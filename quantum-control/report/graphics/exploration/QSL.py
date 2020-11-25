import matplotlib.pyplot as plt

scale = 0.5/0.36537 #Conversion scale for time --> Time[ms]
filename = "QSL"

beta = []
t = []
data = open(filename+".txt", "r")
data.readline()
line = data.readline()
while line:
    ws = line.split('\t')
    beta.append(float(ws[0]))
    t.append(scale*float(ws[1]))
    line = data.readline()
    
plt.plot(beta,t, 's-', color="orange")
plt.xlabel(r"Interatomic interaction, $\beta$")
plt.ylabel("Estimated QSL [ms]")

plt.savefig(filename+".pdf")