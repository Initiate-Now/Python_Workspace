'''*****************************************************
* Name     : SimpleCalculator.py
* Category : Basic Data Types (integers, floats, strings, booleans),
             Variables, Operators, and Basic Input/Output using
             print() and input().
* Program  : Write a Python script that asks the user to input two
             numbers, performs addition, subtraction, multiplication
             and division, and prints the result in a formatted way.
* Author   : Navin Chakravarthy Kamalakannan
*********************************************************'''
# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing arithmetic operations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined (division by Zero)"

# Printing results using formatted output
print("\nResults:")
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} * {num2} = {product}")
print(f"{num1} / {num2} = {quotient}")