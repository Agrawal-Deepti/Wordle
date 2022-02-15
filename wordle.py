import ui as ui
import dictionary as dictionary
"""
Author - Deepti Agrawal
Assignment 4 - Create a free GitHub account and deploy the prior assignments' code and improve the game to keep 
statistics of plays to be displayed when the user quits.

Prior Assignments - Modular Wordle game
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
            print('You guessed the correct hidden word in %d trials! \n' % (trial + 1))
            won_game = 1
            guessed_in_trial = trial + 1
            break
        elif (trial + 1) == attempts_allowed:
            print('Game Ended - You could not guess the hidden word in %d attempts, Try luck other time! \n'
                  % attempts_allowed)
        else:
            print("Guessed word did not matched at %s , attempt left %d, please try again! "
                  % (is_char_matched, (attempts_allowed - trial - 1)))  # inform user which char are correct,
            # incorrect, or at wrong spot
    return won_game, guessed_in_trial


def determine_accuracy_per_character(is_char_matched, hidden_word, guessed_word):
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


def build_stat_and_print(fstat, fwon_game, fguessed_in_trial):
    fstat["won_game"] = fstat["won_game"] + fwon_game
    fstat["number_of_game_played"] = fstat["number_of_game_played"] + 1
    fstat["current_streak"] = fstat["won_game"]
    fstat["max_streak"] = fstat["won_game"]
    fstat["win_percent"] = (fstat["won_game"] * 100)/fstat["number_of_game_played"]
    if fguessed_in_trial > 0:
        fstat["guessDistribution"][str(fguessed_in_trial)] = fstat["guessDistribution"][str(fguessed_in_trial)] + 1
    print('Number of Games Played %d\nWin percentage %d%%\nGuess Distribution %s\n'
          % (fstat["number_of_game_played"], fstat["win_percent"], str(fstat["guessDistribution"])))


while True:  # After success or failure, user will be presented with a new challenge
    won_game, guessed_in_trial = start_wordle_game()
    build_stat_and_print(stat, won_game, guessed_in_trial)

