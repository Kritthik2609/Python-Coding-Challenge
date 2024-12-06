"""
Author: Kritthik
Date: 06-12-2024
Description: Program to define a module to find Fibonacci Numbers and import the module to another program.
"""
def fibonacci_numbers(n):
    list = []
    num1 = 0
    num2 = 1

    for i in range(n):
        list.append(num1)
        num1, num2 = num2, num1 + num2
    return list
