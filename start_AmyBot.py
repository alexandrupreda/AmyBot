import aiml
import os

kernel = aiml.Kernel()

kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")

kernel.setPredicate("amy_name", "AmyBot")
kernel.setPredicate("amy_short","Amy")
kernel.setPredicate("creator", "Alexandru Preda")
kernel.setPredicate("location", "Uni of Essex, in Colchester")

#kernel.setPredicate("bot_car_brand", "Tesla")
#kernel.setPredicate("bot_favorite_weather", "chilly")


# kernel now ready for use
while True:
    message = raw_input("User: ")
    if message == "exit":
        exit()
    else:
        bot_response = kernel.respond(message)
        print "AmyBot: " + bot_response
        # Do something with bot_response