"""To print all chracter of a string in a line"""

string = input("Enter a string: ")
while string != "":
    print(string[0], end=" ")
    string = string[1:]
