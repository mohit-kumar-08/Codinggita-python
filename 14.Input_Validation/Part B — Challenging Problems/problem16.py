"""Calculator Input Validation"""

number_1 = -3
number_2 = 38
operator = "@"

while operator not in "+-*/":
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    operator = input("Enter the operator: ")
    if operator == "/":
        while number_2 == 0:
            number_2 = int(input("Enter second number: "))
else:
    if operator == "+":
        print(number_1 + number_2)
    elif operator == "-":
        print(number_1 - number_2)
    elif operator == "*":
        print(number_1 * number_2)
    else:
        print(number_1 / number_2)
