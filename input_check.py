import sys
import os
import commands

currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "


# checks input for any special keywords
def checkUserInputForAction(message):
    if checkForLearnKeyPhrase(message):
        commands.learn()
        return True
    if checkForResetKeyPhrase(message):
        commands.resetBrain()
        return True


def checkForLearnKeyPhrase(message):
    if ("lets learn" in message) or ("learn something new" in message):
        print(console + "\'learn\' command detected...")
        return True


def checkForResetKeyPhrase(message):
    if "reset" in message:
        print(console + "\'reset\' command detected...")
        user_input = raw_input("Are you sure you want to reset the brain?(yes/no) ")
        if yesAnswer(user_input):
            print(console + "Resetting...")
            return True


def yesAnswer(prompt):
    if not prompt == "no" or not "n" in prompt:
        return True
    else:
        return False
