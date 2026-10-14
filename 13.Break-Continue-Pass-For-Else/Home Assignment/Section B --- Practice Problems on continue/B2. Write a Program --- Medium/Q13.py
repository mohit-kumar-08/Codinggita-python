"""Remove a Chosen Character from Display"""

string = input("Enter a string: ")
character_to_remove = input("Enter the character to remove: ")

for i in string:
    if i == character_to_remove:
        continue
    print(i, end="")
