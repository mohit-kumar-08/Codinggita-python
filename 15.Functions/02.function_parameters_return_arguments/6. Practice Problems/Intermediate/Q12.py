"""to define a function, count_digits(number)"""

number = input("Enter a number: ")

def count_digits(number):
    count = 0
    for i in number:
        count += 1
    return count

print(count_digits(number))