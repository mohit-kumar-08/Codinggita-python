"""Weekday or Weekend"""

day_number = int(input("Enter day number: "))

match day_number:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
