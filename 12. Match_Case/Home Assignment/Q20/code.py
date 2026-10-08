"""Simple Calculator"""

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        print(f'Result = {first_number + second_number}')
    case '-':
        print(f'Result = {first_number - second_number}')
    case '*':
        print(f'Result = {first_number * second_number}')
    case '/':
        match second_number:
            case 0:
                print("Result = 0")
            case _:
                print(f'Result = {first_number / second_number}')
    case _:
        print('Invalid Operator')
