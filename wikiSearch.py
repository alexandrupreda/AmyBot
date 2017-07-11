# https://pypi.python.org/pypi/wikipedia/
import wikipedia
from nltk import tokenize

import commands


# TODO: CHECK WIKIPEDIA FILE, for BeautifulSoup error

# uses
# https://stackoverflow.com/questions/9474395/how-to-break-up-a-paragraph-by-sentences-in-python
# https://github.com/goldsmith/Wikipedia
def wiki(entry):
    print "Searching online for " + entry + "..."
    counter = 1
    try:
        wikiPage = wikipedia.page(entry)
        print wikipedia.summary(entry, sentences=1)
        prompt = raw_input("This one, " + wikiPage.title + "?(yes/no): ")
        if noAnswer(prompt):
            counter = 0
            wikiPage = wikiSearch(entry)
    except:
        wikiPage = wikiSearch(entry)

    if wikiPage is None:
        print "I'll cancel the search then..."
        return

    summary = wikiPage.summary
    summaryList = tokenize.sent_tokenize(summary)
    while counter < len(summaryList):
        print summaryList[counter]
        counter += 1
        if counter % 2 == 0:
            prompt = raw_input("\nMore?(yes/no): ")
            if noAnswer(prompt):
                break

    prompt = raw_input("Do you want me to write this down for later?(yes/no): ")
    if yesAnswer(prompt):
        writeToWikipediaResultsFile(entry, wikiPage)


def writeToWikipediaResultsFile(entry, wikiPage):
    filename = "aiml_files\\wikipedia_results.aiml"
    stringToAdd = "\n\t<category>"
    stringToAdd += "\n\t<pattern>"
    stringToAdd += "IM INTERESTED IN " + entry.upper()
    stringToAdd += "</pattern>"
    stringToAdd += "\n\t<template>"
    stringToAdd += wikipedia.summary(wikiPage.title, sentences=5)
    stringToAdd += "</template>" + "\n\t</category>" + "\n</aiml>"

    stringToAdd = stringToAdd.encode('ascii', 'ignore').decode('ascii')
    stringToAdd = str(stringToAdd)

    commands.deleteLastLineFromFile(filename)
    fileToWrite = open(filename, "a")
    fileToWrite.write(stringToAdd)
    fileToWrite.close()

    print "Ok, I took note"


def wikiSearch(entry):
    searchResults = wikipedia.search(entry)
    print "This is what I found..."
    for result in searchResults:
        print result
    prompt = raw_input("\nwhich result? ")
    if prompt == "none" or prompt == "cancel":
        return None
    return wikipedia.page(prompt)


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