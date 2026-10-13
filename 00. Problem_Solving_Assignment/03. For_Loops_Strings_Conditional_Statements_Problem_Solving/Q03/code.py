"""To calculate of character's in words"""

string = input("Enter a string: ")

vowels = 0
consonant = 0
digit = 0
special_characters = 0

for i in string:
    if i.lower() in 'aeiou':
        vowels += 1
    elif 'a' < i.lower() <= 'z':
        consonant += 1
    elif 48 <= ord(i) <= 57:
        digit += 1
    else:
        special_characters += 1

if vowels > consonant or vowels > digit or vowels > special_characters:
    print("Vowels")
elif consonant > vowels or consonant > digit or vowels > special_characters:
    print("Consonants")
elif digit > vowels or digit > consonant or digit > special_characters:
    print("Digits")
else:
    print("Special Characters")
