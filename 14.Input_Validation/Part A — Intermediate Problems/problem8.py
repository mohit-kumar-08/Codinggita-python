"""Username Validation"""

username = input("Enter username: ").strip()
for i in username:
    if i == " ":
        has_space = True
    else:
        has_space = False

while len(username) < 5 or has_space:
    username = input("Enter username: ").strip()
else:
    print("Accepted username:", username)
