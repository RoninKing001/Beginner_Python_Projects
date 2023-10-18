### ******************** The Simple Password Generator ********************
### ********** About this Project
"""
This is a quick fun project to play flip the coin, Heads or Tails.
It's also designed to reinforce your knowledge on how to use the random module.
"""
### ********** Code begins here

# Importing
import random
import string

"""

The string module in Python is a built-in module that provides a collection of string constants that can be useful 
for various tasks, including generating passwords. It's often used in conjunction with other modules like random to 
create random passwords.

Using this module makes it easy for you, so you don't have to create variables with all letter, digits and symbols.

In a later project I will include an updated version of the password generator that includes the secret module.
This module is better for password generators. 

"""

# Simple Greeting
print("------------------------------------------------------------------------------------------")
print("Welcome To The Simple Password Generator 🤫")
print("------------------------------------------------------------------------------------------")

# User Input
length = int(input("Enter the desired password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(f"Generated Password: {password}")

"""

string.ascii_letters: A string containing all ASCII letters (both uppercase and lowercase).
string.digits: A string containing all ASCII decimal digits (0-9).
string.punctuation: A string containing all punctuation characters.
"""