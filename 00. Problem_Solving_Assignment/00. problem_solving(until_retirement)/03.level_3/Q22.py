"""Sum of Digits"""

number = input("Enter a number: ")
sum = 0
for i in range(len(number)):
    sum += int(number[i])
print(sum)
