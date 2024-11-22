"""
Author: Kritthik
Date: 22-11-2024
Description: Program to construct patterns of stars (*), using a nested for loop.
"""
#Increasing Triangle

n = int(input("Enter the number of rows: "))

for i in range (n):
    for j in range(i+1):
        print("*", end=" ")
    print("")

#Decreasing Triangle

n = int(input("Enter the number of rows: "))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print(" ")


#Hill Pattern

n = int(input("Enter the number of rows: "))

for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range((i*2)-1):
        print("*",end=" ")
    print(" ")

#Reverse Hill Pattern

n = int(input("Enter the number of rows: "))

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range((i*2)-1):
        print("*", end=" ")
    print(" ")



