"""
Author: Kritthik
Date: 19-10-2024
Description: Simple desktop calculator using Python. Only the five basic arithmetic operators.
Output: Enter the first number:5
Enter the second number:24
Enter the third number:26
The sum of num1 and num2 is: 29
The difference when num2 is subtracted from num1 is: -19
The product of num1 and num2 is: 120
The quotient when num1 is divided by num2 is: 0.20833333333333334
The remainder when num1 is divided by num2 is: 5
The result of (num1 + num2) * num3 / 2 is: 377.0
"""
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

print("The sum of num1 and num2 is:", num1 + num2 )
print("The difference when num2 is subtracted from num1 is:", num1 - num2)
print("The product of num1 and num2 is:", num1*num2)
print("The quotient when num1 is divided by num2 is:", num1/num2)
print("The remainder when num1 is divided by num2 is:",num1%num2 )

result = (num1 + num2) * num3 / 2
print("The result of (num1 + num2) * num3 / 2 is:", result)