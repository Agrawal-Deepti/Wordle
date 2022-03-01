import random
import unittest

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


def is_five_Letter_word_exist(word: str):
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



