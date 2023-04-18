# The xx Calendar - a command line calendar management system.
# By Robert Barinov, TUM

import sys
import json

# Checks whether the provided command line arguments are valid. 
def validateInput():
    if len(sys.argv) < 2:
            print("Error: You have to include at least one day/argument!")
            return
    elif len(sys.argv) > 2:
            print("Error: Too many arguments!")
            return
    cmd = sys.argv[1].lower()
# This part chooses the action depending on the given parameters.
    if cmd == "mo" or cmd == "tu" or cmd == "we" or cmd == "th" or cmd == "fr":
        parseDay()
        return
    elif cmd == "today":
        return
    else:
        print("Please run a valid option.")

def parseDay():
#    file = open("./data.json")
#    data = json.load(file)
#    print(data)
#    file.close()
    file = open("./data.json")
    print(file.read())
# Starting point of the program.
validateInput()
