"""Product Quantity and Price"""

product_quantity = int(input("Enter the quantity of the product: "))
product_price = int(input("Enetr the price of product: "))

if product_quantity < 0 and product_price < 0:
    while product_quantity < 0 and product_price < 0:
        product_quantity = int(input("Enter the quantity of the product: "))
        product_price = int(input("Enetr the price of product: "))
        print()
if product_quantity < 0:
    while product_quantity < 0:
        product_quantity = int(input("Enter the quantity of the product: "))
        print()
if product_price < 0:
    while product_price < 0:
        product_price = int(input("Enetr the price of product: "))
        print()
print(f"Total Cost: Rs.{product_quantity * product_price}")
print()
