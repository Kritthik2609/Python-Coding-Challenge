"""
Author: Kritthik
Date: 30-11-2024
Description: Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
"""
def factorial(number):
    if number >= 0:
        if number == 0:
            return 1
        else:
            return number * factorial(number - 1)

number = int(input("Enter a number: "))
custom = factorial(number)

print("The factorial of entered number is:", custom)