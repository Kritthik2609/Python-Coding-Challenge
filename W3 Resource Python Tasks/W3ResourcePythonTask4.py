"""
Author: Kritthik
Date: 30-11-2024
Description: Write a Python program to reverse a string.
"""
def reverse_a_string(string):
    return string[::-1]

word = input("Enter a random word: ")
custom = reverse_a_string(word)
print("The reverse of the entered string is:",custom)
