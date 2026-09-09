character = input("Enter a character: ")
print(ord(character))
if 65 <= ord(character) <= 90:
    print("Uppercase alphabet")
elif 97 <= ord(character) <= 122:
    print("Lowercase alphabet")
elif 48 <= ord(character) <= 57:
    print("Digit")
elif 33 <= ord(character) <= 126:
    print("Special character")