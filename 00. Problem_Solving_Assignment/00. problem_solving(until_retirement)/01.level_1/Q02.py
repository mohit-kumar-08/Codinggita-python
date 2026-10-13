"""Maximum of Two Numbers"""

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

if number1 > number2:
    print(number1)
elif number2 > number1:
    print(number2)
else:
    print(f'{number1} and {number2}')
