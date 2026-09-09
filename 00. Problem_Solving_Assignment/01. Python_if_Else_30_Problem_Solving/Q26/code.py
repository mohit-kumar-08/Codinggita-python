day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if year % 400 == 0:
    leap_year = True
elif year % 4 == 0 and year % 100 != 0:
    leap_year = True
else:
    leap_year = False

if 0 < day <= 31 and 0 < month <= 12:
    if leap_year is True and month == 2:
        if day <= 29:
            print("Valid")
        elif day <= 28:
            print("Invalid")
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31:
            print("Valid")
        else:
            print("Invalid")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")