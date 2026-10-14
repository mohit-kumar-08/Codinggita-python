"""Validate Month and Day"""

month = -1
day = -1
while month < 1 or month > 12 or day > 31 or day < 1:
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
else:
    print("Day and Month Accepted")
