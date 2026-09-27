"""To analyze and calculate discount on products"""

total_price = 0
total_discount = 0
discount_of_10 = 0
discount_of_15 = 0
discount_of_20 = 0


for i in range(1, 11):
    price = int(input(f"Enter price of product {i}: "))
    total_price += price

    if price >= 5000:
        discount_of_20 += 1
        discount = (price / 100) * 20
        total_price -= discount
        total_discount += discount
    elif price >= 3000:
        discount_of_15 += 1
        discount = (price / 100) * 15
        total_price -= discount
        total_discount += discount
    elif price >= 1000:
        discount_of_10 += 1
        discount = (price / 100) * 10
        total_price -= discount
        total_discount += discount

print(f"Final price is {total_price}")
print(f"Total Discount is {total_discount}")