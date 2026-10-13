"""Reverse a Number"""

number = input("Enter a number: ")
result = ""
if number[0] == "-":
    result += "-"
    number = number[1:]
for i in range(len(number) - 1, -1, -1):
    result += number[i]
result = int(result)
print(result)
