"""Deposit Validation"""

balance = 2000
deposite_amount = -5
while deposite_amount < 0:
    deposite_amount = int(input("Enter the amount to deposit: "))
else:
    balance += deposite_amount
    print(balance)
