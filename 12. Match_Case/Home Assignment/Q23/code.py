"""ATM Withdrawl"""

account_type = int(input("Enter account type: "))
amount = int(input("Enter ammount: "))

match account_type:
    case 1:
        if amount > 0:
            print("Savings Account")
            print("Withdrawl Request Accepted")
        else:
            print("Invalid Amount")
    case 2:
        if amount > 0:
            print("Current Account")
            print("Withdrawl Request Accepted")
        else:
            print("Invalid Amount")