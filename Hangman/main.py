### ******************** The Simple Password Generator ********************
### ********** About this Project
"""
This is a quick fun project to play flip the coin, Heads or Tails.
It's also designed to reinforce your knowledge on how to use the random module.
"""
### ********** Code begins here

# Importing
import random
from words_list import words
from hangman_art import logo
from hangman_art import stages

"""

The string module in Python is a built-in module that provides a collection of string constants that can be useful 
for various tasks, including generating passwords. It's often used in conjunction with other modules like random to 
create random passwords.

Using this module makes it easy for you, so you don't have to create variables with all letter, digits and symbols.

In a later project I will include an updated version of the password generator that includes the secret module.
This module is better for password generators. 

"""

### ---------- Stage 1
print(logo)

### ---------- Stage 2
chosen_word = random.choice(words)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# print(f'Pssst, the solution is {chosen_word}.') # For testing purposes

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(f"You win. The word was: {chosen_word}")

    print(stages[lives])