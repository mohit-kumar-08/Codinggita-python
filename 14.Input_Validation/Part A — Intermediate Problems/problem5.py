"""Password Length"""

password = input("Enter password: ").strip()
while len(password) < 8:
    password = input("Enter password: ").strip()
print("Password Accepted")
