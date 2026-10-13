"""Leap Year (Simple Rule)"""

year = int(input("Enter a year: "))
if year % 4 == 0 and year % 400 == 0:
    print("leap year")
else:
    print("not a leap year")
