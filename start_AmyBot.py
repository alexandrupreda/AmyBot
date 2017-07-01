import aiml
import os
import sys
import time
from autocorrect import spell

console = "CONSOLE: "

def spellChecker(message):
    new_message = ""
    for word in message.split():
        word = spell(word)
        new_message = new_message + word + " "
    return new_message

def checkUserInputForAction(message):
    return
    # Restart
    # if ("restart" in message):
    #     print console + "AmyBot is restarting..."
    #     time.sleep(2)
    #     os.execl(sys.executable, sys.executable, *sys.argv)



def checkResponseForAction(message):
    #Shutdown
    if ("bye" in message):
        print console + "AmyBot has shutdown"
        exit()


kernel = aiml.Kernel()

kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")

kernel.setPredicate("amy_name", "AmyBot")
# kernel.setPredicate("amy_short","Amy")
# kernel.setPredicate("creator", "Alexandru Preda")
# kernel.setPredicate("location", "Uni of Essex, in Colchester")

#kernel.setPredicate("bot_car_brand", "Tesla")
#kernel.setPredicate("bot_favorite_weather", "chilly")


# kernel now ready for use
print console + "AmyBot is operational..."
while True:
    user_message = raw_input("User: ")
    checkUserInputForAction(user_message)
    new_user_message = spellChecker(user_message)

    bot_response = kernel.respond(new_user_message)
    print "AmyBot: " + bot_response
    # Do something with bot_response
    checkResponseForAction(bot_response.lower())




