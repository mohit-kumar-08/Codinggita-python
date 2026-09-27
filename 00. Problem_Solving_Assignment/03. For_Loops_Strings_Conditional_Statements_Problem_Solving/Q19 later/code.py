"""To check the security of a sentence"""

string = input("Enter a string: ")
checks = 0

for i in string:
    if i == ".":
        checks += 1
    elif i == "@":
        checks += 1
    elif '0' <= i <= "9":
        checks += 1
    