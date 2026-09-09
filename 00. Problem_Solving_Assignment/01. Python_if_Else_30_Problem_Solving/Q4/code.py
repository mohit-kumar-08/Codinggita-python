number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

if number_1 < number_2 and number_1 < number_3:
    print(f'{number_1} is smaller')
elif number_2 < number_1 and number_2 < number_3:
    print(f'{number_2} is smaller')
elif number_3 < number_1 and number_3 < number_2:
    print(f'{number_3} is smaller')
elif number_1 == number_2 and number_1 < number_3:
    print(f'{number_1} is smaller')
elif number_1 == number_3 and number_1 < number_2:
    print(f'{number_1} is smaller')
elif number_2 == number_3 and number_2 < number_1:
    print(f'{number_2} is smaller')
else:
    print(f'{number_1} is smaller')
