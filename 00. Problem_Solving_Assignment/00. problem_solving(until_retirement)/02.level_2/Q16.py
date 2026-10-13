"""Product 1 to N"""

product = 1
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    product *= i
print(product)
