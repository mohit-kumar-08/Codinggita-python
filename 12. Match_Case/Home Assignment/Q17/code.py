"""ATM with Account Type"""

account_type = int(input("Enter account type: "))
print("""
1 → Check Balance
2 → Deposit
3 → Withdraw
""")
account_operation = int(input("Enter operation: "))

match account_type:
    case 1:
        match account_operation:
            case 1:
                print("Savings Account")
                print("Check Balance Selected")
            case 2:
                print("Savings Account")
                print("Deposit Selected")
            case 3:
                print("Savings Account")
                print("Withdrawl Selected")
            case _:
                print("Invalid Operation")
    case 2:
        match account_operation:
            case 1:
                print("Current Account")
                print("Check Balance Selected")
            case 2:
                print("Current Account")
                print("Deposit Selected")
            case 3:
                print("Current Account")
                print("Withdrawl Selected")
            case _:
                print("Invalid Operation")
    case _:
        print("Invalid Account Type")
