import os
import sys
import wikiSearch
import traceback


currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "

#learn commands
def learnCommand():
    print(console +"This is a developer option. PROCEED WITH CARE!")

    fileName = raw_input(console +"File name: ")
    fileName = "aiml_files\\" + fileName + ".aiml"
    print console + "Accessing " + fileName + "..."


    stringToAdd = ""

    while True:
        stringToAdd += "\n\t<category>"
        stringToAdd += "\n\t<pattern>"
        pattern = raw_input(console + "pattern: ")
        stringToAdd += pattern.upper() + "</pattern>"
        context = raw_input(console + "context?(yes/no): ")
        if context == "yes" or context=="y":
            stringToAdd += "\n\t<that>"
            that = raw_input(console + "context: ")
            stringToAdd += that.upper() + "</that>"

        stringToAdd += "\n\t<template>"
        template = raw_input(console + "template: ")
        stringToAdd += template + "</template>" + "\n\t</category>"

        userInput = raw_input("Another entry?(yes/no): ")
        if userInput == "no" or userInput=="n":
            break

    stringToAdd += "\n\n\t</topic>" + "\n</aiml>"

    deleteLastLineFromFile(fileName)
    deleteLastLineFromFile(fileName)
    fileToWrite = open(fileName, "a")
    fileToWrite.write(stringToAdd)
    fileToWrite.close()

    print console + "End of \'learn\' function"

#required for learnCommand()
#imported from https://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python
def deleteLastLineFromFile(fileName):
    file = open(fileName, "r+")

    # Move the pointer (similar to a cursor in a text editor) to the end of the file.
    file.seek(0, os.SEEK_END)

    # This code means the following code skips the very last character in the file -
    # i.e. in the case the last line is null we delete the last line
    # and the penultimate one
    pos = file.tell() - 1

    # Read each character in the file one at a time from the penultimate
    # character going backwards, searching for a newline character
    # If we find a new line, exit the search
    while pos > 0 and file.read(1) != "\n":
        # here's the pos
        pos -= 1
        file.seek(pos, os.SEEK_SET)

    # So long as we're not at the start of the file, delete all the characters ahead of this position
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()

    file.close()

#interested in command
def interestedInCommand(message):
    message=message.lower()
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