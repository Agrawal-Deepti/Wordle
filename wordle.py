import ui as ui
import dictionary as dictionary
import unittest
"""
Author - Deepti Agrawal
Assignment 5 - Test automation using unit testing.

Design a program that would allow a user to enter their word as an input, and then indicate whether the letters matched
with the expected 5 letter words from dictionary 
Important Note - Please download 'http://mathcenter.oxford.emory.edu/site/math117/probSetAllTogether/words.txt' 
and keep words.txt in workspace to make program work 
"""


def start_wordle_game():
    """
    Main method to start game. Fetches hidden word, finds user input is valid, determines char location is correct
    or not and displays appropriate message to user
    Parameters: None
    Returns: None
    """
    # Hidden word to guess
    print('\nStarting New Game, Good Luck!')
    won_game = 0
    hidden_word = dictionary.fetch_random_five_letter_word().lower()  # Hidden word to guess

    guessed_words = []  # Guessed words to cover scenario if user enters any prior word,
    # they are warned to enter a new word without reducing from the word count.

    is_char_matched = ['"', '"', '"', '"', '"']  # mechanisms to indicate whether a letter
    # is in the correct spot, incorrect spot, or not in any spot.

    attempts_allowed = 6  # allowed attempt to guess hidden word
    guessed_in_trial = 0
    for trial in range(attempts_allowed):
        guessed_word = ui.get_word_from_user(len(hidden_word), guessed_words)
        guessed_words.append(guessed_word)  # keep track of guessed words

        # to determine letter is in the correct spot, incorrect spot, or not in any spot
        determine_accuracy_per_character(is_char_matched, hidden_word, guessed_word)

        if hidden_word == guessed_word:
            print(f'You guessed the correct hidden word in {(trial + 1)} trials! \n')
            won_game = 1
            guessed_in_trial = trial + 1
            break
        elif (trial + 1) == attempts_allowed:
            print(f'Game Ended - You could not guess the hidden word in {attempts_allowed} attempts, '
                  f'Try luck other time!\n')
        else:
            print(f"Guessed word did not matched at {is_char_matched} , attempt left {(attempts_allowed - trial - 1)}"
                  f", please try again! ")  # inform user which char are correct,
            # incorrect, or at wrong spot
    return won_game, guessed_in_trial


def determine_accuracy_per_character(is_char_matched, hidden_word: str, guessed_word: str):
    """
    Determines accuracy of each char in guessed word
        - correct spot - letter itself
        - not in any spot - "
        - incorrect spot - `
        - If a letter is repeated in the entered word and neither is in the correct location, the first letter will be
        marked with the incorrect location symbol ` and the rest with " symbol to indicate they are extra
    Parameters: is_char_matched([char]) - placeholder to show accuracy of char,
        hidden_word(str) - hidden word for game,
        guessed_word(str) - user inputted word
    Returns: None
    """
    # to determine letter is in the correct spot, incorrect spot, or not in any spot
    for index in range(len(guessed_word)):
        if guessed_word[index] == hidden_word[index]:
            is_char_matched[index] = guessed_word[index]  # correct spot
        elif guessed_word[:index].__contains__(guessed_word[index]):
            is_char_matched[index] = '"'  # If a letter is repeated in the entered word and
            # if neither is in the correct location then the rest with " symbol to indicate they are extra.
        elif hidden_word.__contains__(guessed_word[index]):
            is_char_matched[index] = '`'  # incorrect spot or If a letter is repeated in the entered word and
            # if neither is in the correct location,the first letter will be marked with the incorrect location symbol `
        else:
            is_char_matched[index] = '"'  # not in any spot


stat = {
    "number_of_game_played": 0,
    "won_game": 0,
    "win_percent": 0,
    "current_streak": 0,
    "max_streak": 0,
    "guessDistribution": {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }
}


def build_stat_and_print(fstat, fwon_game: int, fguessed_in_trial: int):
    fstat["won_game"] = fstat["won_game"] + fwon_game
    fstat["number_of_game_played"] = fstat["number_of_game_played"] + 1
    fstat["current_streak"] = fstat["won_game"]
    fstat["max_streak"] = fstat["won_game"]
    fstat["win_percent"] = (fstat["won_game"] * 100)/fstat["number_of_game_played"]
    if fguessed_in_trial > 0:
        fstat["guessDistribution"][str(fguessed_in_trial)] = fstat["guessDistribution"][str(fguessed_in_trial)] + 1
    print(f'Number of Games Played {fstat["number_of_game_played"]}\nWin percentage {fstat["win_percent"]}%\n'
          f'Guess Distribution {str(fstat["guessDistribution"])}\n')


def start():
    while True:  # After success or failure, user will be presented with a new challenge
        won_game, guessed_in_trial = start_wordle_game()
        build_stat_and_print(stat, won_game, guessed_in_trial)


if __name__ == "__main__":
    start()


class WordleTest (unittest.TestCase):
    def test_determine_accuracy_per_character_positive(self) -> None:
        """determine accuracy of character in word"""
        char_matched = ['"', '"', '"', '"', '"']
        determine_accuracy_per_character(char_matched, "being", "gains")
        self.assertEquals(char_matched, ['`', '"', "i", "n", '"'])

    def test_determine_accuracy_per_character_negative(self) -> None:
        """determine accuracy of character in word"""
        char_matched = ['"', '"', '"', '"', '"']
        determine_accuracy_per_character(char_matched, "being", "gains")
        self.assertNotEquals(char_matched, ['"', '"', "i", "n", '"'])

    def test_build_stat_positive(self) -> None:
        """determine accuracy of character in word"""
        statInput = {
            "number_of_game_played": 0,
            "won_game": 0,
            "win_percent": 0,
            "current_streak": 0,
            "max_streak": 0,
            "guessDistribution": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0
            }
        }
        statOutput = {
            "number_of_game_played": 1,
            "won_game": 1,
            "win_percent": 100,
            "current_streak": 1,
            "max_streak": 1,
            "guessDistribution": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 1,
                "6": 0
            }
        }
        build_stat_and_print(statInput, 1, 5)
        self.assertEquals(statInput, statOutput)
