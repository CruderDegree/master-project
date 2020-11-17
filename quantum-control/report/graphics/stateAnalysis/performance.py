import matplotlib.pyplot as plt
from math import sqrt

data = open('performanceData.txt', 'r')
data.readline()

gridpoints = 5

grid = [0] * 5
timeUp = [0] * 5
timeLow = [0] * 5
timeErrUp = [0] * 5
timeErrLow = [0] * 5

for i in range(5):
    line = data.readline()
    words = line.split('\t')
    grid[i] = float(words[0])
    timeLow[i] = float(words[1]) + 0.5*(float(words[2]) - float(words[1]))
    timeUp[i] = float(words[3]) + 0.5*(float(words[4]) - float(words[3]))
    timeErrLow[i] = float(words[2]) - float(words[1])
    timeErrUp[i] = float(words[4]) - float(words[3])
data.close()

times = timeUp.copy()
timesErr = [0] * gridpoints
for i in range(len(timeUp)):
    times[i] -= timeLow[i]
    timesErr[i] = sqrt(timeErrLow[i]*timeErrLow[i] + timeErrUp[i] * timeErrUp[i])
    
plt.plot(grid, times, 'm-s', markersize=7.5)
plt.xlabel("Grid size")
plt.ylabel("Performance time [s]")
plt.xscale("log", basex=2)
filename = "PerformanceTime"
plt.savefig(filename+".pdf")