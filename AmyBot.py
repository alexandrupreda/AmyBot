# aiml is pyAIML, (aka Program Y), an AIML interpreter implemented in Python, creted by Cort Danger Stratton
# https://github.com/creatorrr/pyAIML
import aiml

import os
import sys
import Tkinter as tk

import input_check   # local file
import output_check  # local file
import IO            # local file


currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "
lib = "std-startup.xml"
brain = "bot_brain.brn"


# clears the audio folder of any previous bot responses audio files
# https://stackoverflow.com/questions/185936/delete-folder-contents-in-python
def emptyAudioFolder():
    folder = os.path.dirname(os.path.realpath(sys.argv[0]))
    folder = os.path.join(folder, "audio_files")
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


def initialiseAmyBot():
    # take the input from the user
    user_message = IO.userInput()

    # check if any action occurs based on user input
    specialKeyword = input_check.checkUserInputForAction(user_message)

    # if special command identified, skip bot response (AIML)
    if specialKeyword:
        os.remove("bot_brain.brn")
        kernel.bootstrap(learnFiles=lib, commands="load aiml b")
        kernel.saveBrain(brain)
        print "Carry on..."
        return

    bot_response = kernel.respond(user_message)
    IO.botOutput(bot_response)

    # Do something with bot_response
    if output_check.checkBotResponseForAction(bot_response.lower(), user_message):
        os.remove("bot_brain.brn")
        kernel.bootstrap(learnFiles=lib, commands="load aiml b")
        kernel.saveBrain(brain)
        print "Carry on..."

# empty the audio_files folder
emptyAudioFolder()

# load the kernel
kernel = aiml.Kernel()

# load brain or relearn files
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles=lib, commands="load aiml b")
    kernel.saveBrain("bot_brain.brn")

# set some initial predicates
kernel.setPredicate("amy_name", "AmyBot")
kernel.setPredicate("amy_short", "Amy")
kernel.setPredicate("creator", "Alexandru Preda")
kernel.setPredicate("name", "Alex")

# kernel now ready for use
print console + "AmyBot is operational..."

# creates an UI for the bot, using Tkinter
# based on http://www.python-course.eu/tkinter_buttons.php
if IO.voiceOnline:
    root = tk.Tk()
    root.title("AmyBot")
    label = tk.Label(root, fg="dark green")
    label.pack()
    button = tk.Button(root, text='Speak', width=30, command=initialiseAmyBot)
    button.pack()
    root.mainloop()
else:
    while True:
        initialiseAmyBot()
