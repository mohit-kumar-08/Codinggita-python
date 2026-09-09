number = int(input("Enter a number: "))

if number < 0:
    print("Negative")
elif number > 100:
    print("Number is above 100")
elif number >= 51:
    print("Number is between 51 and 100")
elif number >= 11:
    print("Number is between 11 and 50")
else:
    print("Number is between 0 and 10")