### ******************** The Is Leap Year Program ********************
### ********** About this Project
"""

This is a program that takes an input from the user and sees if the year that is inputted is a leap_year year or not
Uses conditionals

Keep in mind:
- on every year that is divisible by 4 with no remainder (Leap)
- except every year that is evenly divisible by 100 with no remainder (Not Leap)
- unless the year is also divisible by 400 with no remainder (Leap)

"""
### ********** Code begins here

# Simple Greeting
print("------------------------------------------------------------------------------------------")
print("Welcome To Leap Year Calendar 🗓️")
print("------------------------------------------------------------------------------------------")

# Input
leap_year = int(input("What year would you like to know is a leap_year year: "))

# Conditionals / Evaluations
if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
    print(f"{leap_year} is a leap_year year")
else:
    print(f"{leap_year} is not a leap_year year")