"""To calculate of 5 customers"""

totl_revenue = 0

for i in range(5):
    subtotal = 0
    ismember = input(f"Is customer {i + 1} a member? (yes/no): ").lower()

    for j in range(3):
        price = int(input(f"Enter price of item {j + 1} of customer {i + 1}: "))
        subtotal += price

    if subtotal >= 2000:
        subtotal -= subtotal * 15 / 100
    elif subtotal >= 1000:
        subtotal -= subtotal * 10 / 100

    if ismember == "yes":
        subtotal -= subtotal * 5 / 100

    totl_revenue += subtotal
    print(f"Final bill of customer {i + 1} is {subtotal}")

print(f"The total revenue of restaurant is {totl_revenue}")
