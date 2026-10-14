"""Stronger Password Rules"""

condition_satisfied = 0
while True:
    condition_satisfied = 0
    password = input("Enter password: ").strip()
    print()
    if len(password) >= 8:
        condition_satisfied += 1
    else:
        print("Password need atleast 8 characters.")
    for character in password:
        if character == " ":
            print("Password should not have whitespace characters.")
            break
    else:
        condition_satisfied += 1
    for character in password:
        if 65 <= ord(character) <= 90:
            condition_satisfied += 1
            break
    else:
        print("There should be atleast one uppercase letter.")
    for character in password:
        if 97 <= ord(character) <= 122:
            condition_satisfied += 1
            break
    else:
        print("There should be atleast one lowercase letter.")
    for character in password:
        if 48 <= ord(character) <= 57:
            condition_satisfied += 1
            break
    else:
        print("There should be atleast one digit.")
    if condition_satisfied == 5:
        break
    print()
print()
print("Password Accepted")
print()
