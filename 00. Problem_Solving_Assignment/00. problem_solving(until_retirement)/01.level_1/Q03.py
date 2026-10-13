"""Maximum of Three Numbers"""

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third number: "))

if number1 > number2 and number1 > number3:
    print(number1)
elif number2 > number1 and number2 > number3:
    print(number2)
elif number3 > number1 and number3 > number2:
    print(number3)
elif number1 > number2 and number1 == number3:
    print(f'{number1} and {number3}')
elif number1 > number3 and number1 == number2:
    print(f'{number1} and {number2}')
elif number2 > number1 and number2 == number3:
    print(f'{number2} and {number3}')
else:
    print(f'{number1}, {number2} and {number3}')
