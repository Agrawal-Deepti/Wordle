import sys

from dictionary import Dictionary


class Run1000Games(object):
    def __init__(self) -> None:
        dictionary = Dictionary()
        for i in range(0, 6000):
            sys.stdout.write(f'{dictionary.fetch_random_five_letter_word().lower()}\n')


run1000Games = Run1000Games()



'''
how to run 1000 games automatically - run below on terminal
python Run1000Games.py | python wordle.py
'''
