"""Banking Menu"""

balance = 10000

option = -1
while option != 4:
    while option < 1 or option > 4:
        print("""
    1. Check balance
    2. Deposit money
    3. Withdraw money
    4. Exit
    """)
        option = int(input("Select a option: "))
    else:
        if option == 1:
            print(balance)
        elif option == 2:
            deposit_amount = -1
            while deposit_amount < 0:
                deposit_amount = int(input("Enter the amount to deposit: "))
            else:
                balance += deposit_amount
        elif option == 3:
            withdrawl_amount = -1
            while withdrawl_amount < 0 or withdrawl_amount > balance:
                withdrawl_amount = int(input("Enter the amount to withdrawl: "))
            else:
                balance -= withdrawl_amount
else:
    print("Banking Menu Exited")
