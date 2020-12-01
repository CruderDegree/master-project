"""
Contains function fileReader
"""

def fileReader(filename: str, *lists, skiplines=0):
    # Reads the file and puts the read items in the given lists
    # filename : Full filename e.g. "HoRun132.txt"
    data = open(filename, "r")

    # Skip lines if any
    for i in range(skiplines):
        data.readline()
        
    line = data.readline()
    
    while(line):
        words = line.split("\t")
        for i in range(len(words)):
                word = words[i]
                lists[i].append(float(word))
        line = data.readline()
    data.close()
    return lists
