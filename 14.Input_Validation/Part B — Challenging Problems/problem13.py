"""Integer Between 1 and 100"""

number = -1
while number < 0 or number > 100:
    number = int(input("Enter a number: "))
else:
    print("Number accepted")
