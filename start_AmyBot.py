import aiml
import os

kernel = aiml.Kernel()

kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")

kernel.setPredicate("user_car_brand", "", )

# kernel now ready for use
while True:
    message = raw_input("User: ")
    if message == "exit":
        exit()
    else:
        bot_response = kernel.respond(message)
        print "AmyBot: " + bot_response
        # Do something with bot_response