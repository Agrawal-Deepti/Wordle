import os
import unittest
from typing import IO
import dictionary


def get_five_letter_words_from_file_convert_to_tuple():
    """
    This function fetches five-letter word list and convert it to tuple
    :return: tuple of file letter words
    """
    return tuple(dictionary.get_five_letter_words_from_file())


def generate_letter_occurrence(file_letter_words: tuple):
    """
    This function obtain letter likelihood, counts the number of times a particular letter appears in
    a given index
    :param file_letter_words: tuple of five-letter words
    :return: letter occurrence(dict)
    """
    letter_occurrence_dict = {}
    for word in file_letter_words:
        for index, letter in enumerate(word):
            if letter not in letter_occurrence_dict.keys():
                letter_occurrence_dict[letter] = [0, 0, 0, 0, 0]
            current_occurrence = letter_occurrence_dict.get(letter)
            current_occurrence[index] = current_occurrence[index] + 1

    return letter_occurrence_dict


def obtain_letter_likelihood(letter_occurrence_dict: dict, dictionary_count: int):
    """
    This function obtain letter likelihood using letter occurrence dict
    by dividing the count by the number of dictionary words
    :param letter_occurrence_dict: occurrence of letter in dictionary words
    :param dictionary_count: count of all words in dictionary
    :return: likelihood of letter (dict)
    """
    for alpha in letter_occurrence_dict:
        letter_occurrence = letter_occurrence_dict.get(alpha)
        for index, occurrence in enumerate(letter_occurrence):
            if occurrence != 0:
                letter_occurrence[index] = letter_occurrence[index]/dictionary_count
        letter_occurrence_dict[alpha] = letter_occurrence
    return letter_occurrence_dict


def sort_word_rank(word_ranks):
    """
    Sorts the dictionary by values and then keys
    :param word_ranks: dictionary of word and weight of letters' occurrence likelihood
    :return: sorted dict
    """
    return sorted(word_ranks.items(), key=lambda x: (-x[1], x[0]))


def write_letter_frequency(letter_occurrence_dict: dict, letter_frequency_file_name: str):
    """
    writes letter frequency to file
    :param letter_occurrence_dict: occurrence dictionary
    :param letter_frequency_file_name: file name
    :return: None
    """
    try:
        letter_frequency_file: IO = open(letter_frequency_file_name, 'w')
    except FileNotFoundError:
        print(f"Can't open file {letter_frequency_file_name}")
    else:
        for letter in sorted(letter_occurrence_dict):
            letter_frequency_file.write(f'{letter}: {letter_occurrence_dict.get(letter)}\n')
    finally:
        letter_frequency_file.close()


def generate_word_ranks(five_letter_words, letter_occurrence_dict: dict):
    """
    Calculate word's weight by multiplying each of its letters' occurrence likelihood.
    :param five_letter_words: all dictionary words
    :param letter_occurrence_dict: occurrence dictionary
    :return: dictionary of word rank
    """
    word_ranks = {}
    for word in five_letter_words:
        rank = 1
        for index, letter in enumerate(word):
            rank = rank * letter_occurrence_dict.get(letter)[index]
        word_ranks[word] = rank
    return word_ranks


def write_word_rank(word_ranks: dict, word_rank_file_name:str):
    """
    Writes word rank to file
    :param word_ranks: dictionary of word rank
    :param word_rank_file_name: file name
    :return: None
    """
    try:
        word_ranks_file: IO = open(word_rank_file_name, 'w')
    except FileNotFoundError:
        print(f"Can't open file {word_rank_file_name}")
    else:
        for index, word in enumerate(sort_word_rank(word_ranks)):
            word_ranks_file.write(f'{index+1},{word[0]},{word[1]}\n')
    finally:
        word_ranks_file.close()


def generate_occurrence_statistics():
    """
    Generate occurrence and rank and writes to file
    :return: None
    """
    five_letter_words = get_five_letter_words_from_file_convert_to_tuple()
    letter_occurrence_dict = generate_letter_occurrence(five_letter_words)
    letter_occurrence_dict = obtain_letter_likelihood(letter_occurrence_dict, len(five_letter_words))
    write_letter_frequency(letter_occurrence_dict, "letterFrequency.csv")
    word_ranks = generate_word_ranks(five_letter_words, letter_occurrence_dict)
    write_word_rank(word_ranks, "wordRank.csv")


generate_occurrence_statistics()


class StatisticsTest (unittest.TestCase):
    def test_get_five_letter_words_from_file_convert_to_tuple_instance_positive(self) -> None:
        """
        test list is getting converted to tuple correctly
        :return: None
        """
        self.assertTrue(type(get_five_letter_words_from_file_convert_to_tuple()), tuple)

    def test_generate_letter_occurrence_positive(self) -> None:
        """
        test letter occurrence is correct
        :return: None
        """
        dictionary_words = ("apple", "adios", "sonar", "rings")
        letter_occurrence = generate_letter_occurrence(dictionary_words)
        self.assertEquals(letter_occurrence.get("a"), [2, 0, 0, 1, 0])

    def test_generate_letter_occurrence_negative(self) -> None:
        """
        test letter occurrence is not incorrect
        :return: None
        """
        dictionary_words = ("apple", "adios", "sonar", "rings")
        letter_occurrence = generate_letter_occurrence(dictionary_words)
        self.assertNotEquals(letter_occurrence.get("d"), [2, 0, 0, 1, 0])

    def test_obtain_letter_likelihood_positive(self) -> None:
        """
        test letter likelihood is correct
        :return: None
        """
        dictionary_words = ("apple", "adios", "sonar", "rings")
        letter_occurrence = generate_letter_occurrence(dictionary_words)
        letter_likelihood = obtain_letter_likelihood(letter_occurrence, len(dictionary_words))
        self.assertEquals(letter_likelihood.get("a"), [0.5, 0, 0, 0.25, 0])

    def test_obtain_letter_likelihood_negative(self) -> None:
        """
        test letter likelihood is not incorrect
        :return: None
        """
        dictionary_words = ("apple", "adios", "sonar", "rings")
        letter_occurrence = generate_letter_occurrence(dictionary_words)
        letter_likelihood = obtain_letter_likelihood(letter_occurrence, len(dictionary_words))
        self.assertNotEquals(letter_likelihood.get("d"), [0.5, 0, 0, 0.25, 0])

    def test_write_letter_frequency_positive(self) -> None:
        """
        test letter frequency file gets created properly
        :return: None
        """
        test_file_path = 'testLetterFrequency.txt'
        dictionary_words = ("apple", "adios", "sonar", "rings")
        letter_occurrence = generate_letter_occurrence(dictionary_words)
        letter_likelihood = obtain_letter_likelihood(letter_occurrence, len(dictionary_words))
        write_letter_frequency(letter_likelihood, test_file_path)
        self.assertTrue(os.path.exists(test_file_path))

    def test_generate_word_ranks_positive(self) -> None:
        """
        test word rank gets calculated correctly
        :return: None
        """
        test_file_path = 'testLetterFrequency.txt'
        dictionary_words = ("apple", "adios", "sonar", "rings")
        letter_occurrence = generate_letter_occurrence(dictionary_words)
        letter_likelihood = obtain_letter_likelihood(letter_occurrence, len(dictionary_words))
        write_letter_frequency(letter_likelihood, test_file_path)
        word_ranks = generate_word_ranks(dictionary_words, letter_likelihood)
        self.assertEquals(word_ranks.get("apple"), 0.001953125)

    def test_generate_word_ranks_Negative(self) -> None:
        """
        test word rank doesn't get's calculated incorrectly
        :return: None
        """
        test_file_path = 'testLetterFrequency.txt'
        dictionary_words = ("apple", "adios", "sonar", "rings")
        letter_occurrence = generate_letter_occurrence(dictionary_words)
        letter_likelihood = obtain_letter_likelihood(letter_occurrence, len(dictionary_words))
        write_letter_frequency(letter_likelihood, test_file_path)
        word_ranks = generate_word_ranks(dictionary_words, letter_likelihood)
        self.assertNotEquals(word_ranks.get("adios"), 0.001953125)

    def test_write_word_rank_positive(self) -> None:
        """
        test word rank files gets created properly
        :return: None
        """
        test_file_path = 'testLetterFrequency.txt'
        dictionary_words = ("apple", "adios", "sonar", "rings")
        letter_occurrence = generate_letter_occurrence(dictionary_words)
        letter_likelihood = obtain_letter_likelihood(letter_occurrence, len(dictionary_words))
        write_letter_frequency(letter_likelihood, test_file_path)
        word_ranks = generate_word_ranks(dictionary_words, letter_likelihood)
        test_file_path_word_rank = 'testWordRank.csv'
        write_word_rank(word_ranks, test_file_path_word_rank)
        self.assertTrue(os.path.exists(test_file_path_word_rank))