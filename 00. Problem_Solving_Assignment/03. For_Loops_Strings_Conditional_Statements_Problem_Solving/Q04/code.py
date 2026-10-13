"""To determin strength of a password."""

for i in range(1, 6):
    conditions_specified = 0
    uppercase_letters = 0
    lowercase_letters = 0
    digits = 0
    special_characters = 0
    password = input(f"Enter password {i}: ")
    if len(password) >= 8:
        conditions_specified += 1
    for i in password:
        if 'a' <= i <'z':
            lowercase_letters += 1
        elif 'A' <= i <= 'Z':
            uppercase_letters += 1
        elif 48 <= ord(i) <= 57:
            digits += 1
        else:
            special_characters += 1
    if lowercase_letters > 0:
        conditions_specified += 1
    if uppercase_letters > 0:
        conditions_specified += 1
    if digits > 0:
        conditions_specified += 1
    if special_characters > 0:
        conditions_specified += 1

    if conditions_specified == 5:
        print("Strong")
    elif conditions_specified >= 3:
        print("Medium")
    else:
        print("Weak")
