"""To count the compressed string"""

string = input("Enter a string: ")
result = ""

current_character = string[0]

count = 0
for i in string:
    result += i
    if i == current_character:
        count += 1
        current_character = i
    else:
        count = 1
        current_character = i
    result += str(count)
print(result)
