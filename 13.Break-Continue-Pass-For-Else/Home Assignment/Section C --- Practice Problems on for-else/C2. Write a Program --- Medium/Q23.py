"""Check Whether a Character Exists"""

string = input("Enter a word: ")
target_character = input("Enter the character to find: ")

for character in string:
    if character == target_character:
        print("Character exists")
        break
else:
    print("Character missing")
