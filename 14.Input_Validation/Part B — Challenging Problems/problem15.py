"""Username and Password Validation"""

username = "a"
password = "a"

for i in username:
    if i == " ":
        has_space = True
    else:
        has_space = False


while len(username) < 5 or has_space or len(password) < 8:
    username = input("Enter username: ")
    password = input("Enter password: ")
else:
    print("Login Successful")

