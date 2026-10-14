"""Number Within a Range"""

number = 5
while number > 50 or number < 10:
    number = int(input("Enter a number: "))
else:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
