string = input("Enter a string: ")
result = 0

for i in string:
    if i == i.upper():
        result += 1
print(result)