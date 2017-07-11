import aiml
import os
import sys

import input_check
import output_check
# from autocorrect import spell

currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "
lib = "std-startup.xml"

#Spell checker
# def spellChecker(message):
#     new_message = ""
#     for word in message.split():
#         word = spell(word)
#         new_message = new_message + word + " "
#     return new_message

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles = lib, commands = "load aiml b")
kernel.setPredicate("amy_name", "AmyBot")
kernel.setPredicate("amy_short","Amy")
kernel.setPredicate("creator", "Alexandru Preda")

# kernel now ready for use
print console + "AmyBot is operational..."
while True:
    user_message = raw_input("User: ")
    # user_message = spellChecker(user_message)
    specialKeyword = input_check.checkUserInputForAction(user_message)

    #if pecial command identified
    #skipping bot response
    if (specialKeyword==True):
        # kernel.bootstrap(learnFiles=lib, commands="load aiml b")
        continue

    bot_response = kernel.respond(user_message)
    print "AmyBot: " + bot_response
    # Do something with bot_response
    if output_check.checkBotResponseForAction(bot_response.lower(), user_message):
        kernel.bootstrap(learnFiles=lib, commands="load aiml b")




