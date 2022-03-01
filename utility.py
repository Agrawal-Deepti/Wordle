import os
import unittest

def extract_fiveletterwords_and_create_newFile(five_letter_word_file_name):
    """
    Filters 5-letter words from dictionary and create new file and store 5-letter words in it
    Parameters: five_letter_word_file_name - file name
    Returns: None
    """
    file = open("words.txt", "r")
    five_letter_word_file = open(five_letter_word_file_name, 'w')
    for line in file:
        if len(line.strip()) == 5:
            five_letter_word_file.write(line)



class UtilityTest (unittest.TestCase):
    def test_extract_fiveletterwords_and_create_newFile_positive(self) -> None:
        """Test file gets created"""
        test_file_path = 'testFiveLetterWords.txt'
        extract_fiveletterwords_and_create_newFile(test_file_path)
        self.assertTrue(os.path.exists(test_file_path))

    def test_extract_fiveletterwords_and_create_newFile_negative(self) -> None:
        """Test file doesnt get created"""
        test_file_path = 'testFiveLetterWords.txt'
        extract_fiveletterwords_and_create_newFile(test_file_path)
        self.assertFalse(not os.path.exists(test_file_path))

    def test_extract_fiveletterwords_and_create_newFile_positive(self) -> None:
        """Test file gets created and logs are getting appended"""
        test_file_path = 'testFiveLetterWords.txt'
        extract_fiveletterwords_and_create_newFile(test_file_path)
        self.assertTrue(open(test_file_path, "r").readline() != "")
        