"""To check whether the string is palindrome or not"""

string = ""
reversed_string = "1"

while string != reversed_string:
    string = input("Enter a string: ")
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    
print(f"{string} is a palindrome.")
