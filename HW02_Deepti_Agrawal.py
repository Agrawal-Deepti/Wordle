"""
Assignment 2 - Wordle game created by Deepti Agrawal
Design a program that would allow a user to enter their word as an input, and then indicate whether the letters matched
with the expected word (assume we have a single hidden word "SONAR" defined in the program).
Pseudocode
Set hidden_word
set guessed_words to empty
set is_word_matched to false
set is_char_matched to _ at all index
set attempts_allowed to 6
set trial counter to 0
While loop until is_word_matched iss true or trial >= 6
    Ask user to guess input and convert it to upper guess for easy comparison  and store in guessed_word
    If guessed_word length not matching with hidden_word
        then inform user,  Ignore guess attempt and continue loop
    If guessed_word contains digit
        then inform user, Ignore guess attempt and continue loop
    If guessed_word contains special character
        then inform user,  Ignore guess attempt and continue loop
    If guessed_word is previously guessed_words
        then inform user,  Ignore guess attempt and continue loop
    Keep track of guessed words for next attempt in guessed_words
    For loop on guessed_word’s each char to determine letter is in the correct spot, incorrect spot, or not in any spot
        If guessed_word[loop counter] is same as hidden_word[loop counter]
            then char is at correct spot so preserve that char at same spot of is_char_matched to show it to user
        If guessed_word[loop counter]  found in hidden_word
            then char is guessed correct but at incorrect spot, preserve with * in is_char_matched to show it to user
        If guessed_word[loop counter]  not found in hidden_word
            then char is not guessed correct, indicate that with _ in is_char_matched to show it to user
    Increase trial attempt
    If hidden_word is same as guessed_word
        then break the while loop
    If all 6 attempts are utilized
        then break the while loop
    Inform user what all chars of guessed_word are at correct spot, incorrect spot, or not in any spot
Finally inform user if word matched or did not match
"""
# Hidden word to guess
hidden_word = "SONAR"  # Hidden word to guess
guessed_words = []  # Guessed words to cover scenario if user enters any prior word,
# they are warned to enter a new word without reducing from the word count.
is_word_matched = False
is_char_matched = ['_', '_', '_', '_', '_']  # mechanisms to indicate whether a letter
# is in the correct spot, incorrect spot, or not in any spot.
attempts_allowed = 6  # allowed attempt to guess hidden word
trial = 0  # to keep track of current attempt
while not is_word_matched:  # keep trying until word isn't matched or all attempts are utilized to guess hidden word
    guessed_word = input("Enter your word as an input to guess:").upper()  # take word from user and change case to
    # upper for easy comparison

    if len(hidden_word) != len(guessed_word):  # if guessed word length is not matching with hidden word, then don't
        # count attempt
        print("Word length is not matching, please try again!")
        continue
    if any(char.isdigit() for char in guessed_word):  # if guessed word contains number, then don't count attempt
        print("Word can not contain number, please try again!")
        continue
    if not guessed_word.isalpha():  # if guessed word contains special char, then don't count attempt
        print("Word can not contain special character, please try again!")
        continue
    if guessed_word in guessed_words:  # if guessed word is already guessed, then don't count attempt
        print("You have already guessed this word, please guess some other word!")
        continue

    guessed_words.append(guessed_word)  # keep track of guessed words

    # to determine letter is in the correct spot, incorrect spot, or not in any spot
    for index in range(len(guessed_word)):
        if guessed_word[index] == hidden_word[index]:
            is_char_matched[index] = guessed_word[index]  # correct spot
        elif hidden_word.__contains__(guessed_word[index]):
            is_char_matched[index] = '*'  # incorrect spot
        else:
            is_char_matched[index] = '_'  # not in any spot

    trial = trial + 1  # if guessed word matches all criteria to ignore attempt then increase attempt by 1
    if hidden_word == guessed_word:
        is_word_matched = True  # user has guessed the word
        break
    elif trial >= attempts_allowed:  # break the loop if all attempts are utilized to guess hidden word but user could
        # not guess word
        break

    print("Guessed word did not matched at %s , attempt left %d, please try again! "
          "[*: Guessed but incorrect spot, _: Incorrect guess]"
          % (is_char_matched, (attempts_allowed - trial)))  # inform user which char are correct, incorrect, or at
    # wrong spot

# Final notification
if is_word_matched:  # if word matched let user know word matched else inform user could not guess word.
    print('You guessed the correct hidden word in %d trials!' % trial)
else:
    print('You could not guess the hidden word, Try luck other time!')
