"""Search for a Number"""

list_of_numbers = map(int, input("Enter numbers: ").split(" "))
target_number = int(input("Enter the number to find: "))

for number in list_of_numbers:
    if number == target_number:
        print("Found")
        break
else:
    print("Not Found")
