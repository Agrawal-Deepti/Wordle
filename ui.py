from dictionary import Dictionary
import sys
import unittest
from unittest.mock import patch
from logger import Logger


class UI(object):
    __logger = Logger("UI")
    __dictionary = Dictionary()

    def __init__(self, word_length: int) -> None:
        self.word_length = word_length
        self.__logger.log("Initializing UI")

    def get_hidden_word_length(self) -> int:
        return self.word_length

    def __str__(self):
        return f"Hidden word length is {self.get_hidden_word_length()}"

    @staticmethod
    def get_user_input() -> str:
        """
        Reads input from user and convert it to lower case
        Parameters: None
        Returns: guessed_word(str) - user inputted word in lower case
        """
        return input("Enter your word as an input to guess:").lower()

    def get_word_from_user(self, guessed_words: list[str]) -> str:
        """
        Validate user inputter word, validate -
            empty string,
            contains digit,
            word length matching with hidden word
            contains only letter, no special symbol
            word in dictionary
            word not in already guessed words
        Parameters:
            guessed_words([str]): previously guessed words
        Returns: guessed_word(str) - user inputted word if passes all criteria as per requirement
        """
        try:
            is_input_valid = False
            guessed_word = ""
            while not is_input_valid:
                guessed_word = self.get_user_input()
                self.__logger.log(f'User input is - {guessed_word}')
                if self.is_input_empty(guessed_word):
                    self.__logger.log(f'Game Ended, thanks for playing wordle game!')
                    self.__logger.log("*******************GAME TERMINATED********************\n")
                    sys.exit("Game Ended, thanks for playing wordle game!")
                if not self.is_word_length_matching_with_hidden_word(guessed_word):
                    # if guessed word length is not matching with hidden word, then don't count attempt
                    print("Word length is not matching, please try again!")
                    self.__logger.log(f'Word length is not matching, please try again!')
                    continue
                if self.is_word_contain_digit(guessed_word):  # if guessed word contains number,
                    # then don't count attempt
                    print("Word can not contain number, please try again!")
                    self.__logger.log(f'Word can not contain number, please try again!')
                    continue
                if not guessed_word.isalpha():  # if guessed word contains special char, then don't count attempt
                    print("Word can not contain special character, please try again!")
                    self.__logger.log(f'Word can not contain special character, please try again!')
                    continue
                if self.is_already_guessed_word(guessed_words, guessed_word):
                    # if guessed word is already guessed, then don't count attempt
                    print("You have already guessed this word, please guess some other word!")
                    self.__logger.log(f'You have already guessed this word, please guess some other word!')
                    continue
                if not self.is_word_contains_in_dictionary(guessed_word):
                    print("Word is not in dictionary, please guess some other word!")
                    self.__logger.log(f'Word is not in dictionary, please guess some other word!')
                    continue

                is_input_valid = True

            self.__logger.log(f'User input - {guessed_word} is valid {is_input_valid}')

            return guessed_word
        except ValueError:
            self.__logger.log(f'User input error')

    @staticmethod
    def is_input_empty(guessed_word: str) -> bool:
        """
        Checks if guessed word is empty or not
        Parameters:
            guessed_word(str): user inputted word to check if it's empty or not
        Returns: True/False (boolean)
            True - if guessed word is empty,
            False - if guessed word is not empty
        """
        return guessed_word == "" or guessed_word is None

    def is_word_length_matching_with_hidden_word(self, guessed_word: str) -> bool:
        """
        Checks if guessed word length is matching with hidden word or not
        Parameters:
            guessed_word(str): user inputted word
        Returns: True/False (boolean)
            True - if length is matching,
            False - if length is not matching
        """
        return self.get_hidden_word_length() == len(guessed_word)

    @staticmethod
    def is_already_guessed_word(already_guessed_words: list[str], guessed_word: str) -> bool:
        """
        Checks if guessed word is in already guessed words
        Parameters:
            already_guessed_words(list[str]): previously guessed words
            guessed_word(str): user inputted word
        Returns: True/False (boolean)
            True - if user inputted word is in already guessed word,
            False - if user inputted word is not in already guessed word
        """
        return guessed_word in already_guessed_words

    @staticmethod
    def is_word_contain_digit(word: str) -> bool:
        """
        Checks if guessed word contain number
        Parameters:
            word(str): user inputted word
        Returns: True/False (boolean)
            True - if user inputted word contains number,
            False - if user inputted word does not contain number
        """
        return any(char.isdigit() for char in word)

    def is_word_contains_in_dictionary(self, word: str) -> bool:
        """
        Checks if guessed word contain in 5-letter dictionary words
        Parameters:
            word(str): user inputted word
        Returns: True/False (boolean)
            True - if user inputted word contains in 5-letter dictionary words ,
            False - if user inputted word does not contain in 5-letter dictionary words
        """
        return word in self.__dictionary.get_five_letter_words_from_file()


class UITest (unittest.TestCase):
    __ui = UI(5)

    def test_is_word_contains_in_dictionary_positive(self) -> None:
        """Test word contains in dictionary"""
        self.assertTrue(self.__ui.is_word_contains_in_dictionary("about"))

    def test_is_word_contains_in_dictionary_negative(self) -> None:
        """Test word does not contain in dictionary"""
        self.assertFalse(self.__ui.is_word_contains_in_dictionary("couch"))

    def test_is_word_contain_digit_positive(self) -> None:
        """Test word contains digit"""
        self.assertTrue(self.__ui.is_word_contain_digit("abou1"))

    def test_is_word_contain_digit_negative(self) -> None:
        """Test word doesnt not contain digit"""
        self.assertFalse(self.__ui.is_word_contain_digit("couch"))

    def test_is_already_guessed_word_positive(self) -> None:
        """Test word is already guessed word"""
        already_guessed_words = ["about"]
        self.assertTrue(self.__ui.is_already_guessed_word(already_guessed_words, "about"))

    def test_is_already_guessed_word_negative(self) -> None:
        """Test word is not guessed word"""
        already_guessed_words = ["about"]
        self.assertFalse(self.__ui.is_already_guessed_word(already_guessed_words, "couch"))

    def test_is_word_length_matching_with_hidden_word_positive(self) -> None:
        """Test guessed word length matching with hidden word"""
        self.assertTrue(self.__ui.is_word_length_matching_with_hidden_word("about"))

    def test_is_word_length_matching_with_hidden_word_negative(self) -> None:
        """Test guessed word length is not matching with hidden word"""
        self.assertFalse(self.__ui.is_word_length_matching_with_hidden_word("boss"))

    def test_is_input_empty_positive(self) -> None:
        """Test input empty"""
        self.assertTrue(self.__ui.is_input_empty(""))

    def test_is_input_empty_negative(self) -> None:
        """Test input is not empty"""
        self.assertFalse(self.__ui.is_input_empty("about"))

    @patch('builtins.input', return_value="about")
    def test_get_user_input_positive(self, mock_input):
        """Test user input"""
        mock_guessed_word = mock_input()
        self.assertTrue(self.__ui.get_user_input() == mock_guessed_word)
