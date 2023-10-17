### ******************** The Word-Based Treasure Island Game ********************
### ********** About this Project
"""

This is a fun little project that uses conditional statements to guide a player through a maze or around an Island, looking for some
Treasure. It is also designed to get you familiar with using and understanding conditional statements.

Tip:
Create a story first and then add part of your story to the conditional statements. This will make it easier to visualise.

The story:

You come to an old abandoned house, You have two doors, The yellow door on the left and a green door on the right.
You go through the yellow door, you are met by the sneaky witch of the Golden Forest, and it's Game Over for you. Sorry.

You go through the Green door, and you are presented by 2 more doors, one red on the left and one blue on the right,
you go through the blue door, you are met by the Ork General and clobbers you all the way back to the past, Game Over for
you, Sorry.

You open the red door and are presented with two bowls, each bowl is filled,
Which one do you choose, one of them is filled with spiders, one is filled with candy.
Your choose the bowl filled with candy, you are automatically transported to the sneaky witch of the Golden Forest,
and it's Game Over for you. Sorry.

You chose the bowl with the spiders, and you feel something metal at
the bottom of the bowl, you grab it, and it's a golden key. The key then transports you to a door, you open the door, and you
find a room full of treasure, You Win. Congratulations!!!!!

"""
from art import ascii_art
### ********** Code begins here

# ASCII Art Welcome
print (ascii_art)

# Welcoming
print("Welcome To Treasure Hunt.")
print("Your Mission Is To Find The Treasure.")

# Conditionals
choice1 = input("You come to an old abandoned house, You have two doors, The yellow door on the left and a green door on the right. 'Left or Right': ").lower()
if choice1 == "right":
    choice2 = input("You are presented by 2 more doors, one red on the left and one blue on the right, 'Left or Right': ").lower()
    if choice2 == "left":
        choice3 = int(input("You open the red door and are presented with two bowls, each bowl is filled, Which one do you choose, one of them is filled with spiders, \none is filled with candy. '1 for spider, 2 for candy': "))
        if choice3 == 1:
            print("You chose the bowl with the spiders, and you feel something metal at the bottom of the bowl, you grab it, and it's a golden key. \nThe key then transports you to a door, you open the door, and you find a room full of treasure, You Win. Congratulations!!!!! ")
        else:
            print("you are automatically transported to The Sneaky Witch of the Golden Forest, and it's Game Over for you. Sorry.")
    else:
        print("You've gone through the blue door, you are met by the Ork General and clobbers you all the way back to the past, Game Over for you, Sorry.")
else:
    print("You've gone through the yellow door, you are met by The Sneaky Witch of the Golden Forest, and it's Game Over for you. Sorry.")
