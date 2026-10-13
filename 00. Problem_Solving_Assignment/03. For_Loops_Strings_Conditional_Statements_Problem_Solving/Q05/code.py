"""To analyze length of each word"""

string = input("Enter a string: ")

for i in string.split():
    print(len(i))
    if len(i) <= 3:
        print("Short")
    elif len(i) <= 6:
        print("Medium")
    else:
        print("Long")
