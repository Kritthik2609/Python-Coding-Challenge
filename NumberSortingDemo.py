"""
Author: Kritthik
Date: 22-11-2024
Description: Input two lists from the user. Merge these lists into a third list such that in the merged list, all even numbers occur first followed by odd numbers. Both the even numbers and odd numbers should be in sorted order.
"""
list1 = [26, 24, 5, 10, 7]
list2 = [25, 23, 4, 9, 6]

list = list1 + list2
print("Total List:",list)

list.sort()
print("Sorted List:",list)

even = []
odd = []

for number in list:
    if number%2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even List:",even)
print("Odd List:",odd)

combined_list = even + odd
print("Combined List:",even + odd)
