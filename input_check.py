import sys
import os
import commands

currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "


# checks input for any special keywords
def checkUserInputForAction(message):
    if checkForLearnKeyPhrase(message):
        commands.learnCommand()
        return True
    if checkForInterestedKeyPhrase(message):
        commands.interestedInCommand(message)
        return True
    return False


def checkForLearnKeyPhrase(message):
    if ("lets learn" in message) or ("learn something new" in message):
        print(console + "\'learn\' command detected...")
        return True


def checkForInterestedKeyPhrase(message):
    if "interested in" in message.lower():
        print(console + "\'interested in\' command detected...")
        return True
