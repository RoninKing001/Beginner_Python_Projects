### ******************** The Hangman Game ********************
### ********** About this Project
"""
This is a fun project Hangman.
It's also designed to reinforce your knowledge on how to use the random module, the
len function, empty list and more.
"""
### ********** Code begins here

# Importing
import random
from words_list import words
from hangman_art import logo
from hangman_art import stages

"""

The imports used above that are below the import random is for importing variables from the other files within the
main folder, these file have the art and word lists in them. This method is used to make your code more readable instead
of adding hundred line of code and making everything more difficult to read.

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