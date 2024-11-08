"""
Author: Kritthik
Date: 08-11-2024
Description: To find second biggest and second smallest number.
"""
limit = int(input("Enter the limit: "))
num = int(input("Enter the number: "))
small = num
big = num
second_small = small
second_big = big

while limit>1:
    num=int(input("Enter the number: "))
    if num>big:
        second_big = big
        big = num
    elif num>second_big:
        second_big = num
    if num<small:
        second_small = small
        small = num
    elif num<second_small:
        second_small = num


    limit = limit - 1

print("The biggest number is", big)
print("The second biggest number is", second_big)
print("The smallest number is", small)
print("The second smallest number is", second_small)






