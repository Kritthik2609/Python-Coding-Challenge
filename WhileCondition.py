"""
Author: Kritthik
Date: 25-10-2024
Output: Enter the number155
The sum of digits of the given number is: 11
"""
num = int(input("Enter the number"))
sum_of_digits = 0
while num>0:
    remainder = num%10
    sum_of_digits = sum_of_digits + remainder
    num = num//10
print("The sum of digits of the given number is:",sum_of_digits)