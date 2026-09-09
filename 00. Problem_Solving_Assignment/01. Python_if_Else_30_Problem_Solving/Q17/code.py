first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

operation = str(input("Enter the operation you want to do: "))

if operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == '/':
    if second_number == 0:
        print("Division by Zero is not possible")
    else:
        print(first_number / second_number)