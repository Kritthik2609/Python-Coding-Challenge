"""
Author: Kritthik
Date: 29-11-2024
Description: Recursive function to multiply two positive numbers.
"""
def multiplying_two_numbers(num1, num2):
    if num1 >= 0 and num2 >= 0:
        if num2 == 1:
            return num1
        else:
            return num1 + multiplying_two_numbers(num1, num2 - 1)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

custom = multiplying_two_numbers(num1, num2)
print("The product of the entered numbers is:", custom)