"""
Author: Kritthik
Date: 18-10-2024
Description: Python program that uses functions from the math module to perform the following operations on a number provided by the user.
Output: Square root of 5: 2.23606797749979
Factorial of 5: 120
5 raised to power 2: 25.0
"""
import math
number = int(input("Enter a number:"))
square_root = math.sqrt(number)
print("Square root of",number,"\b:",square_root)
factorial = math.factorial(number)
print("Factorial of",number,"\b:",factorial)
power = math.pow(5,2)
print("5 raised to power 2","\b:",power)