"""To calculate Final Price"""

price = int(input("Enter price of the item: "))

if price >= 2000:
    final_price = price - price * 20 / 100
else:
    final_price = price

print(final_price)