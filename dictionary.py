import random
import unittest
from logger import Logger
from utility import Utility


class Dictionary(object):
    __logger = Logger("Dictionary")

    def __init__(self):
        self.already_used_five_letter_hidden_words = []

    def __str__(self):
        return f"Already used five letter hidden words are {self.already_used_five_letter_hidden_words}"

    @staticmethod
    def get_five_letter_words_from_file():
        """
        Filters 5-letter words from dictionary and return in array
        Parameters: None
        Returns: five-letter words ([str])
            Array of 5-letter words
        """
        five_letter_words = []
        five_letter_words_file_name = "fiveLetterWords.txt"
        utility = Utility()
        utility.extract_fiveletterwords_and_create_newFile(five_letter_words_file_name)
        file = open(five_letter_words_file_name, "r")
        for line in file:
            five_letter_words.append(line.strip().lower())
        return five_letter_words

    def is_hidden_word_already_used(self, new_hidden_word):
        self.already_used_five_letter_hidden_words
        if len(self.get_five_letter_words_from_file()) == len(self.already_used_five_letter_hidden_words):
            self.already_used_five_letter_hidden_words = []
            Logger("dictionary").log(f'All hidden words are utilized, resetting already used five letter words!')
        is_already_used = new_hidden_word in self.already_used_five_letter_hidden_words
        if new_hidden_word not in self.already_used_five_letter_hidden_words:
            self.already_used_five_letter_hidden_words.append(new_hidden_word)
        return is_already_used

    def fetch_random_five_letter_word(self):
        """
        Returns random 5-letter word from dictionary
        Parameters: None
        Returns: random word(str)
            random 5-letter word from dictionary
        """
        five_letter_words = self.get_five_letter_words_from_file()
        new_hidden_word = random.choice(five_letter_words)
        while self.is_hidden_word_already_used(new_hidden_word):
            self.__logger.log(f'Hidden word already used - {new_hidden_word}, fetching new word!')
            new_hidden_word = random.choice(five_letter_words)
        return new_hidden_word

    def is_five_Letter_word_exist(self, word: str):
        """
        Checks if 5-letter word exist or not
        Parameters:
            word(str): word to check in 5 letter dictionary
        Returns: True/False (boolean)
            True - if word exist in 5-letter dictionary words
            False - if word does not exist in 5-letter dictionary words
        """
        return word in self.get_five_letter_words_from_file()

    if __name__ == "__main__":
        get_five_letter_words_from_file()


class DictionaryTest(unittest.TestCase):

    def test_fetch_random_five_letter_word_positive(self) -> None:
        """Test fetched random five-letter word is not none"""
        self.assertIsNotNone(fetch_random_five_letter_word())

    def test_fetch_random_five_letter_word_length_check_positive(self) -> None:
        """Test length of random letter word is equals to five"""
        self.assertEqual(len(fetch_random_five_letter_word()), 5)

    def test_fetch_random_five_letter_word_length_check_negative(self) -> None:
        """Test length of random letter word is not equals to five"""
        self.assertNotEquals(len(fetch_random_five_letter_word()), 6)

    def test_is_five_Letter_word_exist_positive(self) -> None:
        """Test five-letter word is exist"""
        self.assertTrue(is_five_Letter_word_exist("about"))

    def test_is_five_Letter_word_exist_negative(self) -> None:
        """Test five-letter word is exist"""
        self.assertFalse(is_five_Letter_word_exist("couch"))

    def test_get_five_letter_words_from_file_positive(self) -> None:
        """Test five-letter word received from dictionary """
        self.assertIn("about", get_five_letter_words_from_file())

    def test_get_five_letter_words_from_file_negative(self) -> None:
        """Test if dictionary contains greater than 5-letter word """
        self.assertNotIn("greater", get_five_letter_words_from_file())

    def test_get_five_letter_words_from_file_size(self) -> None:
        """Test size of the returned list is greater then zero"""
        self.assertGreater(len(get_five_letter_words_from_file()), 0)

    def test_is_hidden_word_already_used_positive(self) -> None:
        """Test hidden word already used"""
        global already_used_five_letter_hidden_words
        already_used_five_letter_hidden_words = ["about"]
        self.assertTrue(is_hidden_word_already_used("about"))

    def test_is_hidden_word_already_used_negative(self) -> None:
        """Test hidden word already not used"""
        global already_used_five_letter_hidden_words
        already_used_five_letter_hidden_words = []
        self.assertFalse(is_hidden_word_already_used("about"))