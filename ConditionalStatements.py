"""
Author: Kritthik
Date: 25-10-2024
Description: Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
Output: Enter the first number5
Enter the second number10
Enter the third number20
The largest number is: 20
"""
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if num1>num2 and num1>num3:
    print("The largest number is:", num1)
elif num2>num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
