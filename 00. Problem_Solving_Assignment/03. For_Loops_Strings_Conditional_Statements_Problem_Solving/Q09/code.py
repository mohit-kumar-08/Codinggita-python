"""To calculate position of a character"""

string = input("Enter a string: ")

for i in string:

    if (string.find(i) + 1) % 2 == 0:
        posi_status = "Even"
    else:
        posi_status = "Odd"

    if i.lower() in 'aeiou':
        char_type = "vowel"
    elif 'a' < i.lower() <= 'z':
        char_type = "consonant"
    elif 48 <= ord(i) <= 57:
        char_type = "digit"
    else:
        char_type = "special character"

    print(f"The character is {i}.")
    print(f"The position of {i} is {string.find(i) + 1}, which is {posi_status}")
    print(f"The character is a {char_type}")
