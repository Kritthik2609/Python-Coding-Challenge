"""
Author: Kritthik
Date: 18-10-2024
Description: Python program that demonstrates the usage of arithmetic, comparison, and logical operators. Perform a few operations and print the results.
Output: Sum= 15 ,Division= 2.0
Is a greater than b?: True
Are a and b equal?: False
Logical AND: True
Logical OR: True
"""
number1 =int(input("Enter the first number:"))
number2 =int(input("Enter the second number:"))
print("Sum=",number1+number2,",Division=",number1/number2)
print("Is a greater than b?:", number1 > number2 )
print("Are a and b equal?:", number1 == number2)
print("Logical AND:", number1>0 and number2>0)
print("Logical OR:", number1>0 or number2>0)