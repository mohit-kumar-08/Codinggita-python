"""To count characters type in a string"""

string = input("Enter a string: ")

uppercase_letters = 0
lowercase_letters = 0
digits = 0
spaces = 0
special_characters = 0

for i in string:
    if 'A' <= i <= 'Z':
        uppercase_letters += 1
    elif 'a' <= i <= 'z':
        lowercase_letters += 1
    elif 48 <= ord(i) <= 57:
        digits += 1
    elif ord(i) == 32:
        spaces += 1
    else:
        special_characters += 1

print("Uppercase Letters:",uppercase_letters)
print("Lowercase Letters:",lowercase_letters)
print("Digits:",digits)
print("Spaces:",spaces)
print("Special Characters:",special_characters)
