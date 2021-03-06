import string


def init(text_input):
    text_input = text_input.lower()
    # text_input = text_input.replace("star", "* ")
    text_input = text_input.replace("let's", "let us")

    text_input = text_input.replace("'m", " am")  # I'm
    text_input = text_input.replace("'re", " are")  # You're
    text_input = text_input.replace("'s", " is")  # He's

    text_input = text_input.replace("'ll", " will")  # He'll

    text_input = text_input.replace("don't", "do not")
    text_input = text_input.replace("won't", "will not")

    text_input = text_input.replace(" ad ", " advertisement ")
    text_input = text_input.replace(" ads ", " advertisement ")

    text_input = text_input.replace(" automobiles ", " cars ")

    # other modifications
    text_input = text_input.replace("can you tell me about", "i am interested in")

    for char in string.punctuation:
        text_input = text_input.replace(char, ' ')
    return text_input
