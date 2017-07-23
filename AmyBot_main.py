import aiml
import os
import sys
import Tkinter as tk

import input_check
import output_check
import IO

# please check that line 389 in wikipedia.py is as follows: lis = BeautifulSoup(html, 'html.parser').find_all('li')
# https://github.com/goldsmith/Wikipedia/commit/50bc236836dc20546af61ea7ca6198c3f039a816
# also, make sure that nltk parser is installed; tokenizers/punkt/english.pickle

currentFile = os.path.basename(sys.argv[0])
console = "CONSOLE(" + currentFile + "): "
lib = "std-startup.xml"
brain = "bot_brain.brn"


# clears the audio folder of any previous bot responses audio files
# https://stackoverflow.com/questions/185936/delete-folder-contents-in-python
def emptyAudioFolder():
    import os, shutil
    folder = os.path.abspath("audio_files")
    print folder
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def initialiseAmyBot():
    # take the input from the user
    user_message = IO.userInput()

    # check if any action occurs based on user input
    specialKeyword = input_check.checkUserInputForAction(user_message)

    # if special command identified, skip bot response (AIML)
    if specialKeyword:
        kernel.bootstrap(learnFiles=lib, commands="load aiml b")
        return

    bot_response = kernel.respond(user_message)
    IO.botOutput(bot_response)

    # Do something with bot_response
    if output_check.checkBotResponseForAction(bot_response.lower(), user_message):
        kernel.bootstrap(learnFiles=lib, commands="load aiml b")
        # kernel.saveBrain(brain)


# empty the audio_files folder
emptyAudioFolder()

# load the kernel
kernel = aiml.Kernel()

# load brain or relearn files
# if os.path.isfile("bot_brain.brn"):
#     kernel.bootstrap(brainFile="bot_brain.brn")
# else:

kernel.bootstrap(learnFiles=lib, commands="load aiml b")
# kernel.saveBrain("bot_brain.brn")

# set some initial predicates
kernel.setPredicate("amy_name", "AmyBot")
kernel.setPredicate("amy_short", "Amy")
kernel.setPredicate("creator", "Alexandru Preda")
kernel.setPredicate("user_name", "")

# kernel now ready for use
print console + "AmyBot is operational..."

# creates an UI for the bot, suing Tkinter
# based on http://www.python-course.eu/tkinter_buttons.php
root = tk.Tk()
root.title("AmyBot")
label = tk.Label(root, fg="dark green")
label.pack()
button = tk.Button(root, text='Speak', width=30, command=initialiseAmyBot)
button.pack()
root.mainloop()
