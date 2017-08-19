# AmyBot
A (hopfully context aware) chatbot under construction, being built by Alexandru Preda.
Uses AIML and Python 2.
Based on A.L.I.C.E (http://alice.pandorabots.com/) and inspired by Betty Bot, created by Sian Dobrin.

University of Essex, 2017

This project contains external libraries or files, which have been attached to the project.
Please note that there is no intention of plagiarism, as each of them have been credited and attached for academic/educational purposes only.

- Slightly modified versions of the files or the original ALICE chatbot have also been added -

Dependencies (to install)
Python 2.7

Dependencies (already attached to the project):
aiml - (aka Program Y), an AIML interpreter implemented in Python, creted by Cort Danger Stratton
https://github.com/creatorrr/pyAIML

gtts - Creates an mp3 file from spoken text via the Google TTS (Text-to-Speech) API
https://pypi.python.org/pypi/gTTS

nltk - The Natural Language Toolkit (NLTK) is a Python package for natural language processing
https://pypi.python.org/pypi/nltk

playsound - Pure Python, cross platform, single function module with no dependencies for playing sounds.
https://pypi.python.org/pypi/playsound/1.2.2

speech_recognition - Library for performing speech recognition
https://pypi.python.org/pypi/SpeechRecognition/

pyaudio - Bindings for PortAudio v19, the cross-platform audio input/output stream library
https://pypi.python.org/pypi/PyAudio

portaudio - required for pyaudio

wikipedia - a Python library that makes it easy to access and parse data from Wikipedia.
https://pypi.python.org/pypi/wikipedia/


[requests and bs4 required by wikipedia.py]
[urllib3, chardet, certifi, idna required by requests]
[six required by nltk]
[gtts_token required by gTTS]
[pyaudio required by speech_recognition]

----------------------------------------------------------------------------------------------------

(voice can be turned on/off by changing the value of 'voiceOnline' in IO.py)

KNOWLEDGE BASE

key_phrases.aiml

[AMY]

[LET US TALK ABOUT *], [* LET US TALK ABOUT *] - assigns topic of conversation
[LET US DISCUSS *], [* LET US DISCUSS *]
[LET US TALK* ]

[HOW ABOUT WE * SOMETHING ELSE], [* CHANGE THE TOPIC], [* LET US TALK ABOUT SOMETHING ELSE]

[WHAT WERE WE TALKING ABOUT]
[TOPIC OF CONVERSATION]

[TIPS]

[*] - unknown queries

hello.aiml

[BYE], [*BYE], [BYE*], [* BYE *]

[GOOD MORNING], [MORNING]

[HELLO],[HELLO *] - induction (YEAH, SYRE, FINE, NO, NOPE, NAH, NOT *)
	+ induction
	- end
[HEY], [HEY*] ,[HI],[HIYA],[WHAT IS UP], [WHAT IS NEW], [YO], [YOU ALRIGHT], [GOOD AFTERNOON]

advertisements.aiml

[* MOST SHOCKING ADVERTISEMENT]

[* FUNNIEST ADVERTISEMENT *]

[DO PEOPLE BUY PRODUCTS *]

[* CELEBRITY ENDORSEMENTS]

[SELL ME THIS PEN]

basic_info.aiml

[* YOUR NAME] //What is your name

[* MEET YOU], [* MEET YOU *] //Nice to meet your

[DO YOU KNOW WHO I AM]

[MY NAME IS *]

cars.aiml

[BUY A CAR], [* BUY A CAR], [BUY A CAR*], [*BUY A CAR*], [* BUYING A CAR], [* BUYING A CAR *]

[I LIKE * CARS]

[DO YOU KNOW WHAT KIND OF CARS I LIKE]

[I LIKE CARS WITH * SEATS]

[I LIKE CARS WITH * ENGINES]

[I THINK * CARS ARE *]

facts.aiml
lyrics.aiml

movies.aiml

[* FAVOURITE FILM/MOVIE] -> conversation

[HAVE YOU SEEN/WATCHED *]

[* HORROR MOVIES]

[* WORST MOVIE/FILM]

music.aiml

[* GOOD SINGER]

[* MUSICAL INSTRUMENTS]

[DO YOU LIKE TO DANCE]

[* MUSIC MAKE YOU FEEL]

[* FAVOURITE SONG] -> conv

[* MUSIC DO YOU LISTEN TO]

weather.aiml

[HAVE YOU CHECKED THE WEATHER FOR *], {HAVE YOU CHECKED THE FORECAST FOR *]

[THE WEATHER * *] //The weather looks good

[* FAVORITE SEASON]

[* CLIMATE CHANGE]

[DO YOU LIKE *] //snow, rain, etc

[WHAT ARE THE SEASONS]

[WHAT IS THE COLDEST SEASON]

[WHAT IS THE HOTTEST SEASON]

[* WEATHER AFFECTS THE WAY PEOPLE *]

[* WINTER ACTIVITY]

[* SEEN SNOW] //have you ever seen snow


wikipedia_results.aiml


FUNCTIONS
'learn'
'reset'
'interested in'
'time'




