"""
Author: Kritthik
Date: 25-10-2024
Description: Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
Output: Enter the first number5
Enter the second number10
10  is greater than  5
"""
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
if num1>num2:
    print(num1," is greater than ", num2)
else:
    print(num2, " is greater than ", num1)