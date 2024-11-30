"""
Author: Kritthik
Date: 30-11-2024
Description: Write a Python function to find the maximum of three numbers.
"""
def maximum_of_three_numbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    return numbers[2]

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

custom = maximum_of_three_numbers(num1, num2, num3)
print("The greatest number is",custom)