"""
Author: Kritthik
Date: 29-11-2024
Description: Recursive function to find the greatest common divisor of two positive numbers.
"""
def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1 % num2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

custom = gcd(num1, num2)
print("The greatest common divisor of the entered numbers is:", custom)