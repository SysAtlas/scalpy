# The xx Calendar - a command line calendar management system.
# By Robert Barinov, TUM

import sys
import json

# Class Task for quick modification of data.
class Parser:
    def __init__(self, day, subject, name, notes):
        self.day = day 
        self.subject = subject 
        self.time = name 
        self.notes = notes 
    def parseDay(self):
        file = open("./data.json")
        data = json.load(file)
        print(self.day)
        print(data)
        file.close()
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
    parser = Parser(command, "", 0, "")
    parser.parseDay()
    return
# Starting point of the program.
validateInput() 