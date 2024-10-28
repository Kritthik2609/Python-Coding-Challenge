"""
Author: Kritthik
Date: 28-10-2024
Description: Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:
    1.Convert Celsius to Fahrenheit
    2.Convert Fahrenheit to Celsius
    3.Exit the program
"""
while True:
    print("\n1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        temperature = int(input("Enter the temperature:"))
        fahrenheit = (temperature*9/5) + 32
        print(temperature, "Celsius is",fahrenheit , "Fahrenheit")

    elif choice == 2:
        temperature = int(input("Enter the temperature:"))
        celsius = (temperature-32)*5/9
        print(temperature, "Fahrenheit is", celsius, "Celsius")

    elif choice == 3:
        break

    else:
        print("Invalid Entry")


