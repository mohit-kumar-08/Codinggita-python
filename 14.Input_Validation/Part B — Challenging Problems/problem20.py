"""Safe Average Calculator"""

number = int(input("Enter the range: "))
while number > 20 or number < 1:
    number = int(input("Enter the range: "))

average = 0
for i in range(number):
    average += int(input("Enter number: "))

print(average / number)
