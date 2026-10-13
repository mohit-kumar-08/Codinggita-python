"""Product of Digits"""

number = input("Enter a number: ")
product = 1
for i in range(len(number)):
    product *= int(number[i])
print(product)
