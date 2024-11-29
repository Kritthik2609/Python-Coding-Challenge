"""
Author: Kritthik
Date: 29-11-2024
Description: Program to find the factorial of a number using Recursion.
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

