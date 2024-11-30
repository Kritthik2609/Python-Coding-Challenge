"""
Author: Kritthik
Date: 30-11-2024
Description: Write a Python function to check whether a number falls within a given range.
"""
def number_in_given_range(num1, num2, number):
    if number > num1 and number < num2:
        return "The number falls within the range"
    else:
        return "The number does not fall within the range"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the last number: "))
number = int(input("Enter a random number: "))

custom = number_in_given_range(num1, num2, number)
print(custom)