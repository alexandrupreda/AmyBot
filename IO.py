import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import sys

import preprocessing

voiceOnline = True

audioNumber = 0


# remember: the Bot uses UK English; keep in mind when writing code, since it differs from US English
def userInput():
    if voiceOnline:
        # Imported from
        # https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
        audio_to_text = ""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            fileName = os.path.dirname(os.path.realpath(sys.argv[0]))
            fileName = os.path.join(fileName, "Chime.mp3")
            fileName = str(fileName)
            playsound.playsound(fileName, True)  # Google notification sound
            print("AmyBot: Listening...")
            audio = r.listen(source)
        try:
            audio_to_text = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("ERROR: Google Speech Recognition could not understand audio")
            exit()
        except sr.RequestError as e:
            print("ERROR: Could not request results from Google Speech Recognition service; {0}".format(e))
            exit()
        user_input = audio_to_text
    else:
        user_input = raw_input("User: ")

    user_input = preprocessing.init(user_input)
    print "User: " + user_input

    return user_input


def botOutput(response):
    print "AmyBot: " + response
    if voiceOnline:
        global audioNumber
        audioNumber = audioNumber + 1
        fileName = os.path.dirname(os.path.realpath(sys.argv[0]))
        fileName = os.path.join(fileName, "audio_files", "bot_response" + str(audioNumber) + ".mp3")
        import wikiSearch
        response = wikiSearch.removeBetweenBrackets(response)
        tts = gTTS(text=response, lang='en')
        tts.save(fileName)
        playsound.playsound(fileName, True)
