"""Divisible Number"""

number = int(input("Enter a number: "))

while not (number % 3 == 0 and number % 5 == 0):
    number = int(input("Enter a number: "))
else:
    print("Accepted number:", number)
