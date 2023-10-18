### ******************** The Famous FizzBuzz Quiz ********************
### ********** About this Project
"""
This is the famous FizzBuzz interview quiz. It's designed to get you to think about how to
solve a particular puzzle, so that the employer can see how you go about solving this.

Remeber to add notes to this exercise so that they can see how you break everything down and work on
one thing at a time.
"""
### ********** Code begins here

# Simple Greeting
print("------------------------------------------------------------------------------------------")
print("Welcome To The Famous FizzBuzz Quiz 💫 👹")
print("------------------------------------------------------------------------------------------")

for number in range(1, 101):
    # This first if statement needs to be checked first to ensure that the most specific condition is evaluated first.
    # if you checked for divisibility by 3 and 5 later, the conditions for divisibility by 3 or 5 would always be true,
    # and you'd never reach the "FizzBuzz" condition.
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number) # This last else statement insures that all other numbers are printed as well.
