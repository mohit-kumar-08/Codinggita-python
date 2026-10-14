"""ATM Withdrawal With Denomination Rules"""

balance = 10000
while True:
    withdrawl_amount = int(input("Enter the amount to withdraw: "))
    if withdrawl_amount < 0:
        continue
    elif withdrawl_amount > balance:
        continue
    elif withdrawl_amount % 100 != 0:
        continue
    else:
        break
balance -= withdrawl_amount
print(f"The withdrawl amount is Rs.{withdrawl_amount}")
print(f"The remaining balance is Rs.{balance}")