import aiml
import os
import sys
import time
from autocorrect import spell

console = "CONSOLE: "

#Spell checker
def spellChecker(message):
    new_message = ""
    for word in message.split():
        word = spell(word)
        new_message = new_message + word + " "
    return new_message

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

def checkForLearnKeyword(message):
    splitted = message.split()
    firstWord = splitted[0].lower()
    if (firstWord == "learn"):
        return True
    else:
        return False

def learnCommand():
    print(console + "\'learn\' command detected...")
    print(console +"This is a developer option. PROCEED WITH CARE!")

    fileName = raw_input(console +"File name: ")
    fileName = "aiml_files\\" + fileName + ".aiml"
    print console + "Accessing " + fileName + "..."

    deleteLastLineFromFile(fileName)
    deleteLastLineFromFile(fileName)
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

    file = open(fileName, "a")
    file.write(stringToAdd)
    file.close()

    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    print console + "End of \'learn\' function"

def checkUserInputForAction(message):
    if (checkForLearnKeyword(message)==True):
        learnCommand()

def checkResponseForAction(message):
    #Shutdown
    if ("bye" in message):
        print console + "AmyBot has shutdown"
        exit()


kernel = aiml.Kernel()

kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")

kernel.setPredicate("amy_name", "AmyBot")
kernel.setPredicate("amy_short","Amy")
kernel.setPredicate("creator", "Alexandru Preda")

#kernel.setPredicate("bot_car_brand", "Tesla")
#kernel.setPredicate("bot_favorite_weather", "chilly")


# kernel now ready for use
print console + "AmyBot is operational..."
while True:
    user_message = raw_input("User: ")
    checkUserInputForAction(user_message)
    new_user_message = spellChecker(user_message)
    #Special command identified
    #skipping bot response
    if (checkForLearnKeyword(new_user_message)==True):
        continue

    bot_response = kernel.respond(new_user_message)
    print "AmyBot: " + bot_response
    # Do something with bot_response
    checkResponseForAction(bot_response.lower())




