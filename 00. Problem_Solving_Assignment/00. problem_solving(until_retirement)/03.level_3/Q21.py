"""Count Digits in a Number"""

number = input("Enter a number: ")
count = 0
for i in range(len(number)):
    if number[i].isdigit():
        count += 1
print(count)
