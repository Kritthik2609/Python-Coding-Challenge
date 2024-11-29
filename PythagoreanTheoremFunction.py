"""
Author: Kritthik
Date: 29-11-2024
Description: A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle. Implement using functions.3
"""
def sides_of_a_triangle(side1, side2, side3):
    sides =[side1, side2, side3]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "The given triangle is a right triangle"
    else:
        return "The given triangle is not a right triangle"

side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

custom = sides_of_a_triangle(side1, side2, side3)
print(custom)
