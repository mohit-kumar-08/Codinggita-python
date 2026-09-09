number = int(input("Enter a number: "))

if number % 3 == 0 and number % 7 == 0:
    print("Its's divisible by both 3 and 7")
elif number % 3 == 0 and number % 7 != 0:
    print("Its's divisible only by 3")
elif number % 7 == 0 and number % 3 != 0:
    print("Its's divisible only by 7")
else:
    print("Its's divisible by neither")