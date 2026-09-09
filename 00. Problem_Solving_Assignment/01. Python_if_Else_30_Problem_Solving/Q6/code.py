number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("Its's divisible by both 5 and 11")
elif number % 5 == 0 and number % 11 != 0:
    print("Its's divisible only by 5")
elif number % 11 == 0 and number % 5 != 0:
    print("Its's divisible only by 11")
else:
    print("Its's divisible by neither")