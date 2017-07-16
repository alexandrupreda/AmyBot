# AmyBot
A (hopfully context aware) chatbot under construction, being built by Alexandru Preda.
Uses AIML and Python 2.
Based on A.L.I.C.E (http://alice.pandorabots.com/) and Betty Bot, created by Sian Dobrin.

All rights reserved.
University of Essex, 2017

(voice can be turned on/off by changing the value of 'voiceOnline' in IO.py)

KNOWLEDGE BASE
key_phrases.aiml

[AMY],[AMYBOT]

[LET US TALK ABOUT *], [* LET US TALK ABOUT *] - assigns topic of conversation
[LET US DISCUSS *], [* LET US DISCUSS *]
[LET US TALK* ]

[* TALK ABOUT SOMETHING ELSE]

[WHAT WERE WE TALKING ABOUT]
[TOPIC OF CONVERSATION]

[TIPS]

[WAKE UP]

[*] - unknown queries

hello.aiml

[BYE], [*BYE], [BYE*], [* BYE *]

[GOOD MORNING], [MORNING]

[HELLO],[HELLO *] - induction (YEAH, SYRE, FINE, NO, NOPE, NAH, NOT *)
	+ induction -> basic questions (SURE, OK, NO)
		+ basic_info
		- end
	- end
[HEY], [HEY*] ,[HI],[HIYA],[WHAT IS UP], [WHAT IS NEW], [YO], [YOU ALRIGHT], [GOOD AFTERNOON]

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




