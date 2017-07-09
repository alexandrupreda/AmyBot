import sys
import os

currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "

def checkResponseForAction(message):
    #Shutdown
    if ("bye" in message):
        print console + "AmyBot has shutdown"
        exit()