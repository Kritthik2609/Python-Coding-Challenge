"""
Author: Kritthik
Date: 06-12-2024
Description: Program to define a module to find Fibonacci Numbers and import the module to another program.
"""
def fibonacci_numbers(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, b + a
