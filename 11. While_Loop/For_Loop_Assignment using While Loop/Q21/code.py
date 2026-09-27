"""To print each character of a string seperately"""

string = input("Enter a string: ")
while string != "":
    print(string[0])
    string = string[1:]
