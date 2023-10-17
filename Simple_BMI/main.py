### ******************** The Simple BMI Calculator ********************
### ********** About this Project
"""
This project / exercise is a quick intro into using floats and basic operators.
"""
### ********** Code begins here

# Simple Greeting
print("Welcome To BMI CALC")

# Inputs
weight = float(input("Please enter your current weight in KG's: "))
height = float(input("Next please enter your height in Meters: "))

# Calculations
bmi_formula = weight / height ** 2

# Output
print("----------------------------------------------------------------------")
print(f"Your current BMI is: {bmi_formula: .2f}") # What is : .2f - This does the same things as the round() function, output to second decimal
print("----------------------------------------------------------------------")
