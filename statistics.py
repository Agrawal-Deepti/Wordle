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
