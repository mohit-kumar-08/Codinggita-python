"""To analyze bank account risk"""

balance = 0
deposit = 0
withdrawl = 0
n = int(input("Enter no. of transaction: "))

for i in range(n):
    amount = int(input(f"What is the amount of transaction {i + 1}: "))
    transaction_type = input("What is your transaction type (D/W): ")

    if transaction_type == 'D':
        balance += amount
        deposit += 1
    elif transaction_type == 'W':
        balance -= amount
        withdrawl += 1
    else:
        print("Invalid Trasnaction Type")

    if balance < 500:
        print("Low Balance")
    elif balance < 0:
        print("Overdraft")
    else:
        print("Normal")

print(f"Total Balance: {balance}")
print(f"Total withdrawls: {withdrawl}")
print(f"Total Deposits: {deposit}")
