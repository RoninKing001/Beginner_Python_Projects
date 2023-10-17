### ******************** The Famous Heads and Tails Coin Toss ********************
### ********** About this Project
"""
This is an update on a quick fun project to play flip the coin, Heads or Tails with the addition to play again.
It's also designed to reinforce your knowledge on how to use the random module and using while loop to play again.
"""
### ********** Code begins here

# Importing
import random

# Simple Greeting
print("------------------------------------------------------------------------------------------")
print("Welcome To Coin Toss, Will It Be Heads Or Tails 🪙")
print("------------------------------------------------------------------------------------------")

# While loop
while True:
    # Variables
    coin_flip = ["heads", "tails"]
    user_choice = input("What side of the coin would you like to choose: 'Heads or Tails': ").lower()

    # Randomly choosing the side of the coin
    toss = random.choice(coin_flip)

    # Conditional Statement/Evaluation
    if user_choice == toss:
        print("-------------------------------------")
        print(f"You win! The coin landed on {toss}")
        print("-------------------------------------")

    else:
        print("-------------------------------------------------")
        print(f"Sorry computer wins. The coin landed on {toss}")
        print("-------------------------------------------------")

    play_again = input("Would you like to play again: 'Yes or No': ").lower()
    if play_again != "yes":
        break