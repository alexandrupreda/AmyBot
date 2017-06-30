import aiml
import os
from autocorrect import spell

def spellChecker(message):
    new_message = ""
    for word in message.split():
        word = spell(word)
        new_message = new_message + word + " "
    return new_message

def checkResponseForAction(message):
    #Shutdown
    if ("bye" in message):
        exit()


kernel = aiml.Kernel()

kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")

# kernel.setPredicate("amy_name", "AmyBot")
# kernel.setPredicate("amy_short","Amy")
# kernel.setPredicate("creator", "Alexandru Preda")
# kernel.setPredicate("location", "Uni of Essex, in Colchester")

#kernel.setPredicate("bot_car_brand", "Tesla")
#kernel.setPredicate("bot_favorite_weather", "chilly")


# kernel now ready for use
while True:
    message = raw_input("User: ")
    new_message = spellChecker(message)

    bot_response = kernel.respond(new_message)
    print "AmyBot: " + bot_response
    # Do something with bot_response
    checkResponseForAction(bot_response.lower())




