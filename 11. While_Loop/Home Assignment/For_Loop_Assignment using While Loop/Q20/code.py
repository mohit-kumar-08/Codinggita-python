"""To print multiplication of all number from 1 to n"""

n = int(input("Enter the ending number: "))
i = 1
product = 1
while i <= n:
    product *= i
    i += 1
print(product)
