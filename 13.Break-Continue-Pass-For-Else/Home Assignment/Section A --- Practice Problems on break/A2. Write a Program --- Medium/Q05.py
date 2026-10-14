"""Find the First Matching Character"""

string = input("Enter a string: ")
target_character = input("Enter the target character: ")

for character in string:
    print(character, end=" ")
    if character == target_character:
        break
