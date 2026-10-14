"""Skip, Stop, or Complete?"""

list_of_numbers = map(int, input("Enter list of numbers: ").split(" "))

for number in list_of_numbers:
    if number == 0:
        continue
    elif number == -1:
        break
    print(number)
else:
    print("All values processed")
