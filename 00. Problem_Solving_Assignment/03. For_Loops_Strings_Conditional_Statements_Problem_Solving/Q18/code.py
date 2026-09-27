"""To analyze last 7 transactions of ATM"""

balance = 0
deposits = 0
withdrawls = 0

for i in range(1, 9):
    trans_amount = int(input("Enter the amount of {i} transaction: "))
    d_or_w = input("Is this a Deposite (yes/no): ").lower()

    if d_or_w == "yes":
        balance += trans_amount
        deposits += 1
    elif d_or_w == "no" and balance < trans_amount:
        print("Withdrawl Rejected.")
    elif d_or_w == "no":
        balance -= trans_amount
        withdrawls += 1
    else:
        print("Invalid Input!")

    print(f"The balance is {balance}Rs.")

    if balance < 1000:
        print("Low Balance")

print(f"The final balance is {balance}Rs.")
print(f"There are {deposits} deposits in last 7 days.")
print(f"There are {withdrawls} withdrawls in last 7 days.")
