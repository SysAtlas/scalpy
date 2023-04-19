# The Scalpy Calendar - a command line calendar management system.
# By Robert Barinov, TUM

import sys
import json

# Class Task for quick modification of data.
class Parser:
    # Two constructors for input and output type commands.
    def __init__(self, day, subject, name, notes):
        self.day = day 
        self.subject = subject 
        self.time = name 
        self.notes = notes 
    def __init__(self, day):
         self.day = day

    def parseDay(self):
        file = open("./data.json")
        filedata = json.load(file)
        file.close()
        data = filedata[self.day]
        for item in data:
            item = dict(item)
            things = ""
            for value in item.values():
                 things = things + " " + str(value)
            print(things)
        return
    def addData(self):
         # TODO
         return

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
       outputCommand(cmd) 
    elif cmd == "today":
        return
    else:
        print("Please run a valid option.")

# Case where we want to print data.
def outputCommand(command):
    parser = Parser(command)
    parser.parseDay()
    return

# Starting point of the program.
validateInput() 