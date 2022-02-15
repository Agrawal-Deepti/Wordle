import random


def get_five_letter_words_from_file():
    """
    Filters 5-letter words from dictionary and return in array
    Parameters: None
    Returns: five-letter words ([str])
        Array of 5-letter words
    """
    five_letter_words = []
    file = open("words.txt", "r")
    for line in file:
        if len(line.strip()) == 5:
            five_letter_words.append(line.strip().lower())
    return five_letter_words


def fetch_random_five_letter_word():
    """
    Returns random 5-letter word from dictionary
    Parameters: None
    Returns: random word(str)
        random 5-letter word from dictionary
    """
    return random.choice(get_five_letter_words_from_file())


def is_five_Letter_word_exist(word):
    """
    Checks if 5-letter word exist or not
    Parameters:
        word(str): word to check in 5 letter dictionary
    Returns: True/False (boolean)
        True - if word exist in 5-letter dictionary words
        False - if word does not exist in 5-letter dictionary words
    """
    return word in get_five_letter_words_from_file()


get_five_letter_words_from_file()
