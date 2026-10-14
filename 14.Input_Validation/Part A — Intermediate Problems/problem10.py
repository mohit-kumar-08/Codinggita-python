"""Limited PIN Attempts"""

secret_pin = 2468
for i in range(3):
    user_pin = int(input("Enter pin: "))
    if user_pin == secret_pin:
        print("PIN accepted")
        break
else:
    print("Access Denied")
