"""To count how many times character a appeared in a string"""

string = input("Enter a string: ")
count = 0
while string != "":
    if string[0] == 'a':
        count += 1
    string = string[1:]
print(count)
