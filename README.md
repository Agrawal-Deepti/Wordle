# Wordle
<h1>Description</h1>
Wordle Game - This project has simplified version of the [Wordle game](https://www.nytimes.com/games/wordle/index.html)
<p>This program allow a user to enter their word as an input, and then indicate whether the letters matched with the expected word
<p>If user gives any word with a space, symbol, or number, or gives a word of different length, they are warned without loosing a trial. 
  If a letter is repeated in the entered word, only the correctly placed letter will be without a mark; if neither is in the correct location, the first letter will be marked with the incorrect location symbol ` and the rest with " symbol to indicate they are extra.
<p>User is informed with letter is in the correct spot, incorrect spot, or not in any spot
<p>Random 5 letter word is selected from dictionary [words.txt](http://mathcenter.oxford.emory.edu/site/math117/probSetAllTogether/words.txt)
<p>After success or failure, user is presented with a new challenge (i.e., a new word is randomly selected from valid dictionary words) until the user gives an empty word to exit the program.
  
  <h1>How to Run Program</h1>
  python wordle.py
