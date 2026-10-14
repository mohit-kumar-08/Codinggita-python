"""Withdrawal Validation"""

balance = 5000
withdrawl_amount = int(input("Enter withdrawl amount: "))

while withdrawl_amount <= 0 or withdrawl_amount > balance:
    withdrawl_amount = int(input("Enter withdrawl amount: "))
else:
    balance -= withdrawl_amount
    print("Current Balance:", balance)
