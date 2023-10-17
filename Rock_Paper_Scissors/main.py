### ******************** The Rock Paper Scissors Game ********************
### ********** About this Project
"""
This project is a refresher on your knowledge on using conditionals and while loops to play the game again.

If you would like to see this game with cool ASCII art the please have a look at my Replit project
https://replit.com/@roninking001/Rock-or-Paper-or-Scissors-or-Game
"""
import random

### ********** Code begins here

# Simple Greeting
print("--------------------------------------------------")
print("Welcome To | Rock | Paper | Scissors!")
print("--------------------------------------------------")


while True:
    user_choice = input("Choose your weapon. 'Rock | Paper | Scissors': ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"You have selected {user_choice}")
    print("--------------------------------------------------")
    print(f"Computer chose {computer_choice}")
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You Lose!"
    print(result)
    play_again = input("Would you like to play again: 'Yes or No': ").lower()
    if play_again != "yes":
        break