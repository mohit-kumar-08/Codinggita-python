"""Count digits in a string"""

string = input("Enter a string: ")
count = 0

for i in string:
    if 48 <= ord(i) <= 57:
        count += 1
print(count)
