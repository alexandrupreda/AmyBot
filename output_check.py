import sys
import os
import commands

currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "


def checkBotResponseForAction(bot_message, user_message):
    # Web Search
    if "web search" in bot_message:
        commands.interestedInCommand(user_message)
        return True
