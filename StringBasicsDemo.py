"""
Author: Kritthik
Date: 19-10-2024
Description: Create, concatenate, and print a string and access a sub-string from a given string.
Output: Enter your first name:Kritthik
Enter your second name:Nair
Kritthik Nair
8
Kritthik
Nair

"""
str1 = input("Enter your first name:")
str2 = input("Enter your second name:")

full_name = str1 +" "+str2
print(full_name)
first_name_length = len(str1)
print(first_name_length)

extract_first_name = full_name[:first_name_length]
extract_last_name = full_name[first_name_length+1:]
print(extract_first_name)
print(extract_last_name)