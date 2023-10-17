### ******************** The Famous Heads and Tails Coin Toss ********************
### ********** About this Project
"""
This is a quick fun project to play flip the coin, Heads or Tails.
It's also designed to reinforce your knowledge on how to use the random module.
"""
### ********** Code begins here

# Importing
import random

# Simple Greeting
print("------------------------------------------------------------------------------------------")
print("Welcome To Coin Toss, Will It Be Heads Or Tails 🪙")
print("------------------------------------------------------------------------------------------")

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