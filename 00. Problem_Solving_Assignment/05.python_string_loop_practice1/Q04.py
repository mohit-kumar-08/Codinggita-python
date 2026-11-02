"""Count a character in a string"""

string = input("Enter the string: ")
substring = input("Enter the character to find: ")
count = 0

for i in string:
    if i == substring:
        count += 1
print(count)
