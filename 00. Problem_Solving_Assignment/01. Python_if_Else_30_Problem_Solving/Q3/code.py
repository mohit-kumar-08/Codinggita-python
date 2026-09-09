number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if number_1 > number_2:
    print(f'{number_1} is larger')
elif number_1 < number_2:
    print(f'{number_2} is larger')
else:
    print("Both are equal")