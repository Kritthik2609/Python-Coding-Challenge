"""
Author: Kritthik
Date: 28-10-2024
Description: Write a program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to:
    Check Balance
    Deposit Money
    Withdraw Money
    Exit
"""
balance_amount=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")

    choice= int(input("Enter your choice:"))
    if choice == 1:
        print(f"The current balance ${balance_amount}")

    elif choice == 2:
        deposit_amount = float(input("Enter the amount:"))
        balance_amount = balance_amount + deposit_amount
        print(f"The deposited amount ${deposit_amount} and "f"The current balance ${balance_amount}")

    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to withdraw:"))
        if withdraw_amount > balance_amount:
            print(f"Insufficient balance")
        else:
            balance_amount = balance_amount - withdraw_amount
            print(f"The amount withdrawn ${withdraw_amount} and "f"The current balance ${balance_amount}")

    elif choice == 4:
        break