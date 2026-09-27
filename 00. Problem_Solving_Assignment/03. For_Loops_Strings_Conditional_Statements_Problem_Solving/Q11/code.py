"""To get info of a username"""

for i in range(1, 6):
    digit = 0
    underscore = 0
    special_character = 0
    classification = ""
    username = input(f"Enter username {i}: ")

    for char in username:
        if ord(char) ==  95:
            underscore += 1
        elif 48 <= ord(char) <= 57:
            digit += 1
        elif not 97 <= ord(char.lower()) <= 122:
            special_character += 1

    print(f"The length of {username} is {len(username)}")
    print(f"The first character of {username} is {username[0]}")
    print(f"There are {digit} digits in {username}")
    print(f"There are {underscore} underscores in {username}")

    if special_character > 0:
        print("Invalid")
    elif digit == 0 or underscore == 0:
        print("Needs Improvement")
    else:
        print("Valid")
    print()
