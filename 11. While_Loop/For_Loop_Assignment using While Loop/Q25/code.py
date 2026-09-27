"""To count no. of uppercase letters in a string"""

string = input("enter a string: ")
count = 0
while string != "":
    if 'A' <= string[0] <= 'Z':
        count += 1
    string = string[1:]
print(count)
