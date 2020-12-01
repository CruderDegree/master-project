"""
This file reads a json file (from QEngine) 
and prints all data attributes stored in the data container file
"""

# Link to common library
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lib import jsonReader

datafilename = "gpe-tester.json"

data = jsonReader.readJson(datafilename)

for key in data.keys():
    print(key)
