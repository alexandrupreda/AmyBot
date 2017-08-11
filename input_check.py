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
    if checkForTimeCommand(message):
        commands.timeCommand()
        return True
    if checkForResetKeyPhrase(message):
        commands.resetBrain()
        return True
    # Shutdown
    if checkForByeCommand(message):
        import IO
        IO.botOutput("Bye bye")
        print console + "AmyBot has shutdown"
        exit()


def checkForLearnKeyPhrase(message):
    if "learn" in message:
        print(console + "\'learn\' command detected...")
        return True


def checkForTimeCommand(message):
    if "time" in message:
        return True


def checkForByeCommand(message):
    if "bye" in message:
        return True


def yesAnswer(prompt):
    if not prompt == "no" or not "n" in prompt:
        return True
    else:
        return False


def checkForResetKeyPhrase(message):
    if "reset" in message:
        import IO
        IO.botOutput("\'reset\' command detected...")
        IO.botOutput("Are you sure you want to reset the brain?(yes/no) ")
        user_input = IO.userInput()
        if yesAnswer(user_input):
            IO.botOutput("Proceeding with reset command...")
            return True