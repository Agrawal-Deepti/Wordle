import os
import unittest
from typing import IO
from logger import Logger


class Utility(object):
    __logger = Logger("utility")

    def __init__(self):
        self.__logger.log("Initializing Utility")

    def __str__(self):
        return "Initializing Utility"

    def extract_fiveletterwords_and_create_newFile(self, five_letter_word_file_name):
        """
        Filters 5-letter words from dictionary and create new file and store 5-letter words in it
        Parameters: five_letter_word_file_name - file name
        Returns: None
        """
        try:
            all_words_file: IO = open("words.txt", "r")
            five_letter_word_file: IO = open(five_letter_word_file_name, 'w')
        except FileNotFoundError:
            self.__logger.log(f"Can't open file words.txt or {five_letter_word_file_name}")
        else:
            for line in all_words_file:
                if len(line.strip()) == 5:
                    five_letter_word_file.write(line)
        finally:
            all_words_file.close()
            five_letter_word_file.close()


class UtilityTest (unittest.TestCase):
    __utility = Utility()

    def test_extract_fiveletterwords_and_create_newFile_positive(self) -> None:
        """Test file gets created"""
        test_file_path = 'testFiveLetterWords.txt'
        self.__utility.extract_fiveletterwords_and_create_newFile(test_file_path)
        self.assertTrue(os.path.exists(test_file_path))

    def test_extract_fiveletterwords_and_create_newFile_negative(self) -> None:
        """Test file doesnt get created"""
        test_file_path = 'testFiveLetterWords.txt'
        self.__utility.extract_fiveletterwords_and_create_newFile(test_file_path)
        self.assertFalse(not os.path.exists(test_file_path))

    def test_extract_fiveletterwords_and_create_newFile_and_write_to_file_positive(self) -> None:
        """Test file gets created and logs are getting appended"""
        test_file_path = 'testFiveLetterWords.txt'
        self.__utility.extract_fiveletterwords_and_create_newFile(test_file_path)
        self.assertTrue(open(test_file_path, "r").readline() != "")
        