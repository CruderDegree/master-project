import json

def readJson(filename):
    # Reads a json file and returns the data as a dictionary for further analysis
    f = open(filename, "r")
    dataDict = json.load(f)
    f.close()

    return dataDict
