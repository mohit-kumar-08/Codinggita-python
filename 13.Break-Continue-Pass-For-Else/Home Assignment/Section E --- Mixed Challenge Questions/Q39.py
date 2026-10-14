"""Find the First Number Divisible by Both 4 and 6"""

list_of_numbers = map(int, input("Enter list of number's: ").split(" "))

for number in list_of_numbers:
    if number < 0:
        continue
    elif number % 4 == 0 and number % 6 == 0:
        print(f"Found: {number}")
else:
    print("No matching number")
