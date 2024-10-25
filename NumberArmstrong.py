"""
Author: Kritthik
Date: 25-10-2024
Output: Enter the number:153
It is an armstrong number
"""
num = int(input("Enter the number:"))
input_number = num
sum_of_cube_of_digits = 0
while num>0:
    remainder = num%10
    sum_of_cube_of_digits = sum_of_cube_of_digits + remainder**3
    num = num//10
if sum_of_cube_of_digits == input_number:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")