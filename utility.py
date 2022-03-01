
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
