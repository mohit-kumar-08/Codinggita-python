"""Unit Converter"""

choice = int(input("Enter choice: "))
value = int(input("Enter value: "))

match choice:
    case 1:
        print(value * 1000, "meters")
    case 2:
        print(value / 1000, "meters")
    case 3:
        print(value * 1000, "grams")
    case 4:
        print(value / 1000, "kilograms")
    case _:
        print("Invalid Choice")
