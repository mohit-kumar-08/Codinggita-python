character = input("Enter a aplhabet: ")

if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print("Vowel")
elif 97 <= ord(character) <= 122:
    print("Consonant")
else:
    print("Invalid input")