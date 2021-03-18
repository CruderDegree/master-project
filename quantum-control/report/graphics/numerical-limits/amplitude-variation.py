import matplotlib.pyplot as plt

control_times = {"2": [], "4": [], "6":[]}
amplitudes = {"2": [], "4": [], "6":[]}
timescale = 0.5/0.36537 # Timescale to convert to ms
#Read data file
filename = "space-data.txt"
data = open(filename, mode='r')
data.readline()
line = data.readline()
while line:
    words = line.split('\t')
    xmax = words[0]
    control_times[xmax].append(float(words[1]))
    amplitudes[xmax].append(float(words[2]))
    line = data.readline()

# Same stuff for both figs
xlabel = "Control duration [ms]"

# Plot T,A graph
fig, ax = plt.subplots()
for xmax in control_times.keys():
    ax.plot([t*timescale for t in control_times[xmax]], amplitudes[xmax], '.-', label=r'$x\in \pm $'+xmax+' '+r"$\mu m$")

ax.set( xlabel=xlabel, 
        ylabel="Max amplitude "+r"$[\mu m]$")
        #title="Max amplitude for "+r"$A\,\sin(3\pi t/T)$")
ax.legend(loc="best")

figname = "amplitude-variation"
fig.savefig(figname+".pdf")
fig.savefig(figname+".png")

# Plot T, A/xmax graph
fig, ax = plt.subplots()
for xmax in control_times.keys():
    ax.plot([t*timescale for t in control_times[xmax]], [A/float(xmax) for A in amplitudes[xmax]], '.-', label=r'$x\in \pm $'+xmax+' '+r"$\mu m$")

ax.set( xlabel=xlabel, 
        ylabel=r"$A/x_{max}$")
        #title="Relative max amplitude for "+r"$A \, \sin(3\pi t/T)$")
#ax.legend(loc="best")

figname = "amplitude-variation-relative"
fig.savefig(figname+".pdf")
fig.savefig(figname+".png")