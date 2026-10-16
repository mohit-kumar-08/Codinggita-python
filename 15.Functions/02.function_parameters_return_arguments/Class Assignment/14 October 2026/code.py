"""To interact with mini bank"""

balance = 30000
withdrawl_amount = 0
deposite_amount = 0

def check_balance():
    return balance 

def withdraw(withdrawl_amount, balance):
    balance -= withdrawl_amount
    return balance

def deposite(deposite_amount, balance):
    balance += deposite_amount
    return balance

print("""
1. Check balance
2. Deposite Money
3. Withdraw Money
""")
option = int(input("Select option: "))

match option:
    case 1:
        print(check_balance())
        print()
    case 2:
        deposite_amount = int(input("Enter the amount to deposite: "))
        print()
        print(f"Deposited Rs.{deposite_amount}")
        print(f"Your balance is Rs.{deposite(deposite_amount, balance)}")
        print()
    case 3:
        withdrawl_amount = int(input("Enter the amount to withdraw: "))
        print()
        print(f"Withdrawled Rs.{withdrawl_amount}")
        print(f"Your balance is Rs.{withdraw(withdrawl_amount, balance)}")
        print()
    case _:
        print("Invalid Option!")
        print()
