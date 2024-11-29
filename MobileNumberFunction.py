"""
Author: Kritthik
Date: 29-11-2024
Description: Program to check whether the given number is a valid mobile number or not using functions.
"""
def mobile_number(number):
    if len(number) == 10 and number[0] in ["9", "8", "7"]:
        return "The given mobile number is valid"
    else:
        return "The given mobile number is invalid"

custom = input("Enter the mobile number: ")
print(mobile_number(custom))






