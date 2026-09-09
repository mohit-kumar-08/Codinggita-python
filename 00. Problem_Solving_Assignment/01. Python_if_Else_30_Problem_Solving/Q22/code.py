balance = int(input("Enter Account Balance: "))
withdrawl = int(input("Enter Withdrawl Amount: "))

if withdrawl > 0 and withdrawl % 100 == 0 and withdrawl < balance and balance - withdrawl >= 500:
    print(f"""
Withdrawal successful
Remaining balance: {balance - withdrawl}""")