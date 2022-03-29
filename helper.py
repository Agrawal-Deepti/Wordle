from statistics import Statistics
from logger import Logger


class Helper(object):
    def __init__(self):
        self.logger = Logger('Helper')
        self.statistics = Statistics()
        five_letter_words = self.statistics.get_five_letter_words_from_file_convert_to_tuple()
        letter_occurrence_dict = self.statistics.generate_letter_occurrence(five_letter_words)
        letter_occurrence_dict = self.statistics.obtain_letter_likelihood(letter_occurrence_dict,
                                                                          len(five_letter_words))
        self.five_letter_word_ranks = self.statistics.generate_word_ranks(five_letter_words, letter_occurrence_dict)

    def __str__(self):
        return f"Total five letter words with ranks are {len(self.get_five_letter_word_ranks())}"

    def get_five_letter_word_ranks(self):
        """
        :return: all five-letter word ranks set by constructor
        """
        return self.five_letter_word_ranks

    @staticmethod
    def is_input_provided(good_letters: str, bad_letters: str, position_of_letters: []):
        """
        Validates if input is provided or not
        :param good_letters: good letter string
        :param bad_letters: bad letter string
        :param position_of_letters: position of letters in word
        :return: True/False
        """
        is_input_provided = False

        if position_of_letters is not None and len(position_of_letters) > 0:
            for letter in position_of_letters:
                if letter != '_':
                    is_input_provided = True
                    break
                else:
                    is_input_provided = False
        else:
            is_input_provided = False

        if not is_input_provided and ((good_letters is None or len(good_letters) == 0 or good_letters == '') and
                                      (bad_letters is None or len(bad_letters) == 0 or bad_letters == '')):
            is_input_provided = False
        else:
            is_input_provided = True
        return is_input_provided

    @staticmethod
    def is_input_valid(good_letters: str, bad_letters: str, position_of_letters: []):
        """
        Validates if input is correct like,
         good letters are not more than 5 char, not digit, is alpha
         bad letters not digit, is alpha
         position of letters are not more than 5, not digit, is alpha or _
         good letters are not in bad letter
         bad letters are not in good letters and position of letters
        :param good_letters: good letter string
        :param bad_letters: bad letter string
        :param position_of_letters: position of letters in word
        :return: True/False
        """
        is_input_valid = True
        if is_input_valid and (len(good_letters) > 5 or good_letters.isdigit() or
                               (good_letters is not None and good_letters != "" and not good_letters.isalpha())):
            is_input_valid = False

        if is_input_valid and (bad_letters.isdigit() or
                               (bad_letters is not None and bad_letters != "" and not bad_letters.isalpha())):
            is_input_valid = False

        if is_input_valid and len(position_of_letters) > 5:
            is_input_valid = False

        if is_input_valid:
            for letter in position_of_letters:
                if letter.isdigit() or (not letter.isalpha() and letter != "_"):
                    is_input_valid = False
                    break
        if is_input_valid:
            for good_letter in good_letters:
                if good_letter in bad_letters:
                    is_input_valid = False
                    break
        if is_input_valid:
            for bad_letter in bad_letters:
                if bad_letter in good_letters:
                    is_input_valid = False
                    break
        if is_input_valid:
            for bad_letter in bad_letters:
                if bad_letter in position_of_letters:
                    is_input_valid = False
                    break

        return is_input_valid

    def search_possible_words_to_use(self, good_letters: str, bad_letters: str, position_of_letters: []):
        """
        It applies all possible filter to suggest words, if no input is provided it gives first 50 words based
        on word rank
        :param good_letters: good letter string
        :param bad_letters: bad letter string
        :param position_of_letters: position of letters in word
        :return: list of all possible words along with rank
        """
        self.logger.log(f"*********New request to suggest words**********")
        good_letters = good_letters.lower()
        bad_letters = bad_letters.lower()
        position_of_letters = [letter.lower() for letter in position_of_letters]
        sorted_final_possible_words_are = {}
        self.logger.log(f"Good letters words are {good_letters}, "
                        f"Bad Letter words are {bad_letters}, "
                        f"Correct letter positions are {position_of_letters}")

        is_input_valid = self.is_input_valid(good_letters, bad_letters, position_of_letters)
        is_input_provided = self.is_input_provided(good_letters, bad_letters, position_of_letters)
        if not is_input_provided:
            self.logger.log(f'No Input provided, so returning top 50 words based on word rank')
            possible_words_to_use = self.get_five_letter_word_ranks()
            sorted_final_possible_words_are = self.statistics.sort_word_rank(possible_words_to_use)
            sorted_final_possible_words_are = sorted_final_possible_words_are[:50]
            self.logger.log(f'{sorted_final_possible_words_are}')
        elif is_input_valid:
            possible_words_to_use = self.get_five_letter_word_ranks()
            self.logger.log(f'Total Five letter words are - {len(possible_words_to_use)}')

            position_based_words_to_use = self.filter_position_based_words(possible_words_to_use, position_of_letters)
            self.logger.log(f'Total Five letter words after applying position based filter are '
                            f'{len(position_based_words_to_use)}')

            words_after_applying_good_letter_filter = self.filter_good_letter_words(position_based_words_to_use,
                                                                                    good_letters)
            self.logger.log(f'Total Five letter words after applying good letter filter are '
                            f'{len(words_after_applying_good_letter_filter)}')

            words_after_applying_bad_letter_filter = self.filter_bad_letter_words(
                                                                        words_after_applying_good_letter_filter,
                                                                        bad_letters)
            self.logger.log(f'Total Five letter words after applying bad letter filter are '
                            f'{len(words_after_applying_bad_letter_filter)}')

            sorted_final_possible_words_are = self.statistics.sort_word_rank(words_after_applying_bad_letter_filter)
            self.logger.log(f'Possible words are {sorted_final_possible_words_are}')
        else:
            self.logger.log("Input is not valid")
        self.logger.log(f"***********************************************")
        return sorted_final_possible_words_are

    def filter_position_based_words(self, word_ranks: dict, position_of_letters: []):
        """
        Filters words based on position of letters
        :param word_ranks: dictionary of words to filter
        :param position_of_letters: position of letters to filter
        :return: filtered words dictionary
        """
        if len(position_of_letters) == 0:
            self.logger.log(f'position of letter is null so not applying filter and returning all elements')
            return word_ranks
        keep_words = set()
        for word in word_ranks:
            is_good_word = False
            for index, letter in enumerate(position_of_letters):
                if letter.lower() == "_" or letter.lower() == word[index].lower():
                    is_good_word = True
                else:
                    is_good_word = False
                    break
            if is_good_word:
                keep_words.add(word)

        self.logger.log(f'Removing all words other than - {keep_words}')
        return {keep_word: word_ranks[keep_word] for keep_word in word_ranks if keep_word in keep_words}

    def filter_bad_letter_words(self, word_ranks: dict, bad_letters: str):
        """
        Filters words based on bad letters
        :param word_ranks: dictionary of words to filter
        :param bad_letters: bad letters
        :return: filtered words dictionary
        """
        if bad_letters is None or bad_letters == "":
            self.logger.log(f'Bad letters is null so not applying filter and returning all elements')
            return word_ranks
        remove_words = set()
        for word in word_ranks:
            for letter in bad_letters:
                if letter.lower() in word.lower():
                    remove_words.add(word)

        if len(remove_words) > 0:
            self.logger.log(f'Removing words as these are bad letter words - {remove_words}')
        else:
            self.logger.log(f'No bad letter words found to remove')

        for remove_word in remove_words:
            word_ranks.pop(remove_word)

        return word_ranks

    def filter_good_letter_words(self, word_ranks: dict, good_letters: str):
        """
        Filters words based on good letters
        :param word_ranks: dictionary of words to filter
        :param good_letters: good letters
        :return: filtered words dictionary
        """
        if good_letters is None or good_letters == "":
            self.logger.log(f'Good letters is null so not applying filter and returning all elements')
            return word_ranks
        good_words = set()
        for word in word_ranks:
            is_good_word = False
            for letter in good_letters:
                if letter.lower() in word.lower():
                    is_good_word = True
                else:
                    is_good_word = False
                    break

            if is_good_word:
                good_words.add(word)

        self.logger.log(f'Removing all words other than - {good_words}')
        return {good_word: word_ranks[good_word] for good_word in word_ranks if good_word in good_words}


'''
For local run
helper = Helper()
helper.search_possible_words_to_use("", "",['a','_','d','_'])
'''
