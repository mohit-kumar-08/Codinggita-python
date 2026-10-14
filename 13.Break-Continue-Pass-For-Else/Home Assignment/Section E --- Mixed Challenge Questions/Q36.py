"""Search and Report"""

list_of_numbers = map(int, input("Enter list of numbers: ").split(" "))
target_number = int(input("Enter target's number: "))

for number in list_of_numbers:
    if number < 0:
        continue
    if number == target_number:
        print("Target found")
        break
else:
    print("Target not found")
