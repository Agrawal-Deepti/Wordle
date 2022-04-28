from logger import Logger
from helper import Helper


class Solver(object):
    def __init__(self) -> None:
        self.logger = Logger('Solver')
        self.good_letters = []
        self.bad_letters = []
        self.position_of_good_letters = ['_', '_', '_', '_', '_']
        self.possible_words = {}
        self.helper = Helper()

    def get_good_letters(self) -> []:
        return self.good_letters

    def get_bad_letters(self) -> []:
        return self.bad_letters

    def get_position_of_good_letters(self) -> []:
        return self.position_of_good_letters

    def append_to_good_letters(self, good_letter) -> None:
        self.good_letters.append(good_letter)

    def append_to_bad_letters(self, bad_letter) -> None:
        self.bad_letters.append(bad_letter)

    def append_position_of_good_letters(self, index: int, good_letter) -> None:
        self.position_of_good_letters[index] = good_letter

    def get_possible_words(self):
        return self.possible_words

    def set_possible_words(self, possible_words: dict) -> None:
        self.possible_words = possible_words

    @staticmethod
    def covert_to_string(char_array: []) -> str:
        return ''.join(char_array)

    def __str__(self) -> str:
        return f"---------------------------------------------\n" \
               f"Bad Letters are - {self.get_bad_letters()}\n" \
               f"Good Letters are - {self.get_good_letters()}\n" \
               f"Position of Good Letters are - {self.get_position_of_good_letters()}\n" \
               f"Possible words are - {self.get_possible_words()}\n" \
               f"----------------------------------------------"

    def solve(self, hidden_word: str, guessed_word: str) -> None:
        """
        This method finds good letters, bad letters, position of good letters and possible good words
        :param hidden_word: hidden word for the game
        :param guessed_word: guessed word by the user
        :return: None
        """
        for index, guessed_letter in enumerate(guessed_word):
            if guessed_letter in hidden_word and guessed_letter not in self.get_good_letters():
                self.append_to_good_letters(guessed_letter)
                self.logger.log(f"Appended {guessed_letter} to good letters")
            elif guessed_letter not in hidden_word and guessed_letter not in self.get_bad_letters():
                self.append_to_bad_letters(guessed_letter)
                self.logger.log(f"Appended {guessed_letter} to bad letters")

            if hidden_word[index] == guessed_letter:
                self.append_position_of_good_letters(index, guessed_letter)
                self.logger.log(f"Added {guessed_letter} to index {index} of position of good letters")

        possible_words = self.helper.search_possible_words_to_use(
                                                    Solver.covert_to_string(self.get_good_letters()),
                                                    Solver.covert_to_string(self.get_bad_letters()),
                                                    self.get_position_of_good_letters())
        self.logger.log(f"Possible words are {possible_words}")
        self.logger.log(self.__str__())
        self.set_possible_words(possible_words)
