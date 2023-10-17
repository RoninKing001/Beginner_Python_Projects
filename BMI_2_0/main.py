### ******************** The BMI 2.0 ********************
### ********** About this Project
"""
This is an updated version of the Simple BMI Calculator,
It uses simple conditionals to evaluate if the BMI is within a certain range
and if it is, it will print out whether you are underweight, normal, overweight or obese

If your BMI is less than 18.5, it falls within the underweight range.
If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range.
If your BMI is 25.0 to 29.9, it falls within the overweight range.
If your BMI is 30.0 or higher, it falls within the obese range.

"""
### ********** Code begins here

# Simple Greeting
print("------------------------------------------------------------------------------------------")
print("Welcome To BMI 2.0 🍔")
print("------------------------------------------------------------------------------------------")

# Inputs
weight = float(input("Please enter your current weight in KG's: "))
height = float(input("Next please enter your height in Meters: "))

# Calculations
bmi_formula = weight / height ** 2

# Conditionals / Evaluations
if bmi_formula <= 18.5:
    print("\n")
    print(f"Your current BMI is {bmi_formula: .2f} which means you fall in the range of being underweight.")
elif bmi_formula <= 24.9:
    print("\n")
    print(f"Your current BMI is {bmi_formula: .2f} which means you fall in the range of being Healthy Weight.")
elif bmi_formula <= 29.9:
    print("\n")
    print(f"Your current BMI is {bmi_formula: .2f} which means you fall in the range of being overweight.")
else:
    print("\n")
    print(f"Your current BMI is {bmi_formula: .2f} which means you fall in the range of being obese.")
