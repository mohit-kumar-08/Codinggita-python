# For only three digit number

number = int(input("Enter the number: "))

sum = 0

sum += number % 10
number = number // 10

sum += number % 10
number = number // 10

sum += number

print(sum)

# For any digit number (Extra)

number = int(input("Enter the number: "))

sum = 0

while number > 0:
    sum += number % 10
    number = number // 10

print(sum)