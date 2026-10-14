"""Stop at a Negative Number"""

numbers = map(int, input("Enter numbers: ").split(" "))

for number in numbers:
    if number < 0:
        break
    print(number, end=" ")
