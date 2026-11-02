"""Find the substring 420"""

number = input("Enter the number: ")
char_of_number = input("Enter the number to find: ")

if char_of_number in number:
    print('Caught')
else:
    print("Escaped")
