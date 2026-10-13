"""Divisible by 3 and 5"""

number = int(input("Enter a number: "))
if number % 5 == 0 and number % 3 == 0:
    print("divisible by 3 and 5")
else:
    print("not divisible by both")
