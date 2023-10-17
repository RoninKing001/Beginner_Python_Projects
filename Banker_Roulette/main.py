### ******************** The Banker Roulette Program ********************
### ********** About this Project
"""
This is a quick fun project to play with some friends to see who will be paying the bill for your next lunch or dinner,
it's also designed to reinforce your knowledge on how to use the random module and it's methods.
"""
### ********** Code begins here

# Importing
import random

# Simple Greeting
print("------------------------------------------------------------------------------------------")
print("Welcome To Banker Roulette 💰")
print("------------------------------------------------------------------------------------------")


# Users Input
user_input = input("What are the name of the people you would like to add to the hat, separate each name with a comma: ").lower()

# Takes away unwanted characters
user_input = user_input.split(", ") # This .split method takes out the comma and the space following the comma

# Using Random Methods
pick = random.choice(user_input).upper() # This .choice method randomly selects a name in user_input and then converts it to uppercase

# Output
print("------------------------------------------------------------------------------------------")
print(f"The lucky winner that's paying for dinner/lunch is {pick}")
print("------------------------------------------------------------------------------------------")