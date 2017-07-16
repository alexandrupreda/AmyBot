import os
import speech_recognition as sr
from gtts import gTTS
import playsound
import time
from tempfile import TemporaryFile

import preprocessing

voiceOnline = True

audioNumber=0

def userInput():
    if voiceOnline:
        # Imported from
        # https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
        audio_to_text = ""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("AmyBot: Listening...")
            audio = r.listen(source)
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            audio_to_text = r.recognize_google(audio)
            print("Input: " + audio_to_text)
        except sr.UnknownValueError:
            print("ERROR: Google Speech Recognition could not understand audio")
            exit()
        except sr.RequestError as e:
            print("ERROR: Could not request results from Google Speech Recognition service; {0}".format(e))
            exit()
        user_input = audio_to_text
        print "User: " + user_input
    else:
        user_input = raw_input("User: ")

    user_input = preprocessing.init(user_input)

    return user_input


def botOutput(response):
    print "AmyBot: " + response
    if voiceOnline:
        global audioNumber
        audioNumber = audioNumber + 1
        fileName = "audio_files\\bot_response +" + str(audioNumber) + ".mp3"
        tts = gTTS(text=response, lang='en')
        tts.save(fileName)
        playsound.playsound(fileName, True)