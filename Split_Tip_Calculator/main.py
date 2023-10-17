### ******************** The Restaurant Split And Tip Calculator ********************
### ********** About this Project
"""
This is a quick fun project to help you split the bill with friends,
it's also designed to reinforce variables and some basic operators.
"""
### ********** Code begins here

# Simple Greeting
print("------------------------------------------------------------------------------------------")
print("Welcome To Restaurant Split and Tip Calculator 💰")
print("------------------------------------------------------------------------------------------")

# Inputs
bill_amount = float(input("What is the bill amount : $"))
tip_percentage = int(input("What is the tip percentage amount you would like to give: E.g. 10, 20, 25: "))
party = int(input("How many people would you like to split the bill with: "))

# Calculations
tip_amount = bill_amount * tip_percentage / 100
bill_total = bill_amount + tip_amount
each_person = bill_total / party

# Output
print("------------------------------------------------------------------------------------------")
print(f"The bill amount is: ${bill_amount}")
print(f"The tip percent you would like to give is: {tip_percentage}%")
print(f"The number of people you would like to split the bill with is: {party}")
print("\n \n")
print(f"The total bill is: ${bill_total}")
print(f"The amount each person needs to contribute is: ${each_person: .2f}")
print("------------------------------------------------------------------------------------------")
