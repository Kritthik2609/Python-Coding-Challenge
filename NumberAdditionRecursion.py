"""
Author: Kritthik
Date: 29-11-2024
Description: Recursive function to add two positive numbers.
"""
def adding_two_numbers(num1, num2):
    if num1 >= 0 and num2 >= 0:
        if num2 == 0:
            return num1
        else:
            return adding_two_numbers(num1 + 1, num2 - 1)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

custom = adding_two_numbers(num1, num2)
print("The sum of the entered numbers is:", custom)