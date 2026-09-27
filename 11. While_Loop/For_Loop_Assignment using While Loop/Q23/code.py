"""To count no. of characters in a string"""

string = input("Enter a string: ")
count = 0
while string != "":
    count += 1
    string = string[1:]
print(count)
