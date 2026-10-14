"""Age Validation"""

age = int(input("Enter age: "))
while age < 0 or age > 120:
    print("Invalid Age")
    age = int(input("Enter age: "))
