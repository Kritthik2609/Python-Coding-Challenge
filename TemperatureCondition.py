"""
Author: Kritthik
Date: 25-10-2024
Description: Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c/5=(f−32)/9
Output: Enter the temperature100
Is this in (C)elsius or (F)ahrenheit?C
100 Celsius is 212.0 Fahrenheit
"""
temperature = int(input("Enter the temperature"))
celsius_or_fahrenheit = input("Is this in (C)elsius or (F)ahrenheit?")
if celsius_or_fahrenheit=="C":
    fahrenheit = ((9/5)*temperature+32)
    print("100 Celsius is", fahrenheit, "Fahrenheit")
elif celsius_or_fahrenheit=="F":
    celsius = (5/9*(temperature-32))
    print("32 Fahrenheit is",celsius, "Celsius")