"""Reverse a string using a loop"""

string = input("Enter a string: ")
reversed_string = ""

while string != "":
    count = 0
    for i in range(len(string)):
        count += 1
        if count == len(string):
            reversed_string += string[i]
            string = string[:len(string) - 1]
print(reversed_string)
