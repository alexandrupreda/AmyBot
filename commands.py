import os
import sys
import wikiSearch
import traceback
import IO

currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "


# learn commands
def learn():
    print console + "This is a developer option. PROCEED WITH CARE!"
    IO.botOutput("What's the topic about")
    fileName = IO.userInput()
    fileName = "aiml_files\\" + fileName + ".aiml"
    print console + "Accessing " + fileName + "..."

    stringToAdd = ""

    while True:
        stringToAdd += "\n\t<category>"
        stringToAdd += "\n\t<pattern>"

        IO.botOutput("What's the pattern?")
        pattern = IO.userInput()
        stringToAdd += pattern.upper() + "</pattern>"

        IO.botOutput("Any context (yes or no): ")
        context = IO.userInput()
        if yesAnswer(context):
            stringToAdd += "\n\t<that>"
            that = raw_input(console + "context: ")
            stringToAdd += that.upper() + "</that>"

        stringToAdd += "\n\t<template>"
        IO.botOutput("What should be the answer?")
        template = IO.userInput()
        stringToAdd += template + "</template>" + "\n\t</category>"

        IO.botOutput("Another entry? (yes or no): ")
        userInput = IO.userInput()
        if noAnswer(userInput):
            break

    stringToAdd += "\n\n\t</topic>" + "\n</aiml>"

    deleteLastLineFromFile(fileName)
    deleteLastLineFromFile(fileName)
    fileToWrite = open(fileName, "a")
    fileToWrite.write(stringToAdd)
    fileToWrite.close()

    print console + "End of \'learn\' function"


# required for learnCommand()
# imported from https://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python
def deleteLastLineFromFile(fileName):
    fileToProcess = open(fileName, "r+")

    # Move the pointer (similar to a cursor in a text editor) to the end of the file.
    fileToProcess.seek(0, os.SEEK_END)

    # This code means the following code skips the very last character in the file -
    # i.e. in the case the last line is null we delete the last line
    # and the penultimate one
    pos = fileToProcess.tell() - 1

    # Read each character in the file one at a time from the penultimate
    # character going backwards, searching for a newline character
    # If we find a new line, exit the search
    while pos > 0 and fileToProcess.read(1) != "\n":
        # here's the pos
        pos -= 1
        fileToProcess.seek(pos, os.SEEK_SET)

    # So long as we're not at the start of the file, delete all the characters ahead of this position
    if pos > 0:
        fileToProcess.seek(pos, os.SEEK_SET)
        fileToProcess.truncate()

    fileToProcess.close()


# interested in command
def interestedInCommand(message):
    message = message.lower()
    characters = 0
    for word in message.split():
        characters += len(word) + 1
        if word == "interested":
            characters += len("in") + 1
            break
    term = message[characters:]
    try:
        wikiSearch.wiki(term)
    except:
        traceback.print_exc()


def timeCommand():
    from datetime import datetime
    IO.botOutput("The time is " + datetime.now().strftime('%H:%M'))

def resetBrain():
    os.remove("bot_brain.brn")
    print(console + "Done. Goodbye!")
    exit()

def yesAnswer(prompt):
    if not prompt == "no" or not "n" in prompt:
        return True
    else:
        return False


def noAnswer(prompt):
    if prompt == "no" or "n" in prompt:
        return True
    else:
        return False
