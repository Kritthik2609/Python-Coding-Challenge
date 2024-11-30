"""
Author: Kritthik
Date: 30-11-2024
Description: Write a Python function to sum all the numbers in a list.
"""
def sum_of_numbers_in_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

nums = int(input("Enter the number of elements: "))
list = []

for j in range(nums):
    x = int(input("Enter the number: "))
    list.append(x)

print(list)

custom = sum_of_numbers_in_list(list)
print("The sum of the numbers in the list is",custom)