"""To calculate fare of bus ticket"""

total_collection = 0

for i in range(8):
    age = int(input(f"Enter passenger {i + 1}'s age: "))
    distance = int(input(f"Enter passenger {i + 1}'s distance: "))
    subtotal = 0

    subtotal = 10 * distance

    if age < 5:
        subtotal = 0
    elif age <= 12:
        subtotal -= subtotal * 50 / 100
    elif age >= 60:
        subtotal -= subtotal * 30 / 100

    total_collection += subtotal

    print(f"The total fare of passanger {i + 1} is {subtotal}")
print(f"The total collection of bus is {total_collection}")
