# https://pypi.python.org/pypi/wikipedia/
import wikipedia
from nltk import tokenize

import commands
import IO

# please check that line 389 in wikipedia.py is as follows: lis = BeautifulSoup(html, 'html.parser').find_all('li')
# https://github.com/goldsmith/Wikipedia/commit/50bc236836dc20546af61ea7ca6198c3f039a816
# also, make sure that nltk parser is installed; tokenizers/punkt/english.pickle


# uses
# https://stackoverflow.com/questions/9474395/how-to-break-up-a-paragraph-by-sentences-in-python
# https://github.com/goldsmith/Wikipedia
def wiki(entry):
    IO.botOutput("Searching online for " + entry + "...")
    sentenceCounter = 1
    try:
        wikiPage = wikipedia.page(entry)
        summaryOneSent = wikipedia.summary(entry, sentences=1)
        summaryOneSent = removeBetweenBrackets(summaryOneSent)
        IO.botOutput(summaryOneSent)
        IO.botOutput("Is this " + wikiPage.title + " you were looking for?(yes or no): ")
        prompt = IO.userInput()
        if noAnswer(prompt):
            sentenceCounter = 0
            wikiPage = wikiSearch(entry)
    except:
        wikiPage = wikiSearch(entry)

    if wikiPage is None:
        IO.botOutput("I'll cancel the search then...")
        return
    summary = wikiPage.summary
    summaryList = tokenize.sent_tokenize(summary)
    while sentenceCounter < len(summaryList):
        if sentenceCounter % 2 == 0 and sentenceCounter != 0:
            IO.botOutput("Would you like more info? (yes or no)")
            prompt = IO.userInput()
            if noAnswer(prompt):
                IO.botOutput("That's it then")
                break
        IO.botOutput(summaryList[sentenceCounter])
        sentenceCounter += 1

    IO.botOutput("Do you want me to write this down for later? (yes or no): ")
    prompt = IO.userInput()
    if yesAnswer(prompt):
        noOfSentences = 3
        if noOfSentences > len(summaryList):
            noOfSentences = len(summaryList)
        writeToWikipediaResultsFile(entry, wikiPage, noOfSentences)


def writeToWikipediaResultsFile(entry, wikiPage,noOfSentences):
    filename = "aiml_files\\wikipedia_results.aiml"
    stringToAdd = "\n\t<category>"
    stringToAdd += "\n\t<pattern>"
    stringToAdd += "* INTERESTED IN " + entry.upper()
    stringToAdd += "</pattern>"
    stringToAdd += "\n\t<template>"
    # it's speculated that count begins from 0
    stringToAdd += wikipedia.summary(wikiPage.title, sentences=noOfSentences-1)
    stringToAdd += "</template>" + "\n\t</category>" + "\n</aiml>"

    #cleanup
    stringToAdd = textCleanUp(stringToAdd)

    commands.deleteLastLineFromFile(filename)
    fileToWrite = open(filename, "a")
    fileToWrite.write(stringToAdd)
    fileToWrite.close()

    IO.botOutput("Ok, I took note. What's next?")


def wikiSearch(entry):
    searchResults = wikipedia.search(entry)
    IO.botOutput("This is what I found...")
    for result in searchResults:
        print result
    IO.botOutput("\nwhich result? (you can cancel if you want) ")
    prompt = IO.userInput()
    if prompt == "none" or prompt == "cancel":
        return None
    try:
        return wikipedia.page(prompt)
    except:
        errorMessage()


def wikiName(entry):
    return wikipedia.page(entry).title


def noAnswer(prompt):
    if prompt == "no" or "n" in prompt:
        return True
    else:
        return False


def yesAnswer(prompt):
    if not prompt == "no" or not "n" in prompt:
        return True
    else:
        return False


def errorMessage():
    IO.botOutput("Something malfunctioned... apologies for that")
    return


def textCleanUp(text):
    text = removeBetweenBrackets(text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = str(text)
    # check for illegal AIML characters
    text = text.replace("&", " and ")
    return text


# https://stackoverflow.com/questions/14596884/remove-text-between-and-in-python
def removeBetweenBrackets(text):
    import re
    text = re.sub("[\(\[].*?[\)\]]", "", text)
    return text