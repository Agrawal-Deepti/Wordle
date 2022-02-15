import dictionary as dictionary
import sys


def get_user_input():
    """
    Reads input from user and convert it to lower case
    Parameters: None
    Returns: guessed_word(str) - user inputted word in lower case
    """
    return input("Enter your word as an input to guess:").lower()


def get_word_from_user(word_length, guessed_words):
    """
    Validate user inputter word, validate -
        empty string,
        contains digit,
        word length matching with hidden word
        contains only letter, no special symbol
        word in dictionary
        word not in already guessed words
    Parameters:
        word_length(int): hidden word length
        guessed_words([str]): previously guessed words
    Returns: guessed_word(str) - user inputted word if passes all criteria as per requirement
    """
    is_input_valid = False
    guessed_word = ""
    while not is_input_valid:
        guessed_word = get_user_input()
        if is_input_empty(guessed_word):
            sys.exit("Game Ended, thanks for playing wordle game!")
        if not is_word_length_matching_with_hidden_word(word_length, guessed_word):
            # if guessed word length is not matching with hidden word, then don't count attempt
            print("Word length is not matching, please try again!")
            continue
        if is_word_contain_digit(guessed_word):  # if guessed word contains number, then don't count attempt
            print("Word can not contain number, please try again!")
            continue
        if not guessed_word.isalpha():  # if guessed word contains special char, then don't count attempt
            print("Word can not contain special character, please try again!")
            continue
        if is_already_guessed_word(guessed_words, guessed_word):
            # if guessed word is already guessed, then don't count attempt
            print("You have already guessed this word, please guess some other word!")
            continue
        if not is_word_contains_in_dictionary(guessed_word):
            print("Word is not in dictionary, please guess some other word!")
            continue

        is_input_valid = True
    return guessed_word


def is_input_empty(guessed_word):
    """
    Checks if guessed word is empty or not
    Parameters:
        guessed_word(str): user inputted word to check if it's empty or not
    Returns: True/False (boolean)
        True - if guessed word is empty,
        False - if guessed word is not empty
    """
    return guessed_word == "" or guessed_word is None


def is_word_length_matching_with_hidden_word(hidden_word_length, guessed_word):
    """
    Checks if guessed word length is matching with hidden word or not
    Parameters:
        hidden_word_length(int): hidden word against which game is getting played
        guessed_word(str): user inputted word
    Returns: True/False (boolean)
        True - if length is matching,
        False - if length is not matching
    """
    return hidden_word_length == len(guessed_word)


def is_already_guessed_word(already_guessed_words, guessed_word):
    """
    Checks if guessed word is in already guessed words
    Parameters:
        already_guessed_words([str]): previously guessed words
        guessed_word(str): user inputted word
    Returns: True/False (boolean)
        True - if user inputted word is in already guessed word,
        False - if user inputted word is not in already guessed word
    """
    return guessed_word in already_guessed_words


def is_word_contain_digit(word):
    """
    Checks if guessed word contain number
    Parameters:
        word(str): user inputted word
    Returns: True/False (boolean)
        True - if user inputted word contains number,
        False - if user inputted word does not contain number
    """
    return any(char.isdigit() for char in word)


def is_word_contains_in_dictionary(word):
    """
    Checks if guessed word contain in 5-letter dictionary words
    Parameters:
        word(str): user inputted word
    Returns: True/False (boolean)
        True - if user inputted word contains in 5-letter dictionary words ,
        False - if user inputted word does not contain in 5-letter dictionary words
    """
    return word in dictionary.get_five_letter_words_from_file()
