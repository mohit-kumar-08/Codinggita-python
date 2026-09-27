"""To calculate prices of products"""

total = 0
budget = 0
regular = 0
premium = 0
luxury = 0

for i in range(1, 9):
    price = int(input(f"Enter price of product {i}"))
    total += price
    if price >= 0:
        if price < 500:
            print("Budget")
            budget += 1
        elif price < 2000:
            print("Regular")
            regular += 1
        elif price < 5000:
            print("Premium")
            premium += 1
        else:
            print("Luxury")
            luxury += 1
    else:
        print("Put Valid Price.")

print(f"Total Amount is {total}")
print(f"Average Amount is {total / 8}")
print(f"{budget} products are in Budget.")
print(f"{regular} products are in Regular.")
print(f"{premium} products are in Premium.")
print(f"{luxury} products are in Luxury.")
