"""Check whether the complete string is a palindrome"""

string = input("Enter a string: ")
for i in range(len(string)):
    if string[i] == string[len(string) - (1 + i)]:
        continue
    else:
        print("no")
        break
else:
    print("yes")
