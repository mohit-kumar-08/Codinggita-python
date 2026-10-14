"""Input Validation Without break"""

number = -1
while number < 0 or number > 10:
    number = int(input("Enter a number: "))
else:
    print("Number Accepted")
