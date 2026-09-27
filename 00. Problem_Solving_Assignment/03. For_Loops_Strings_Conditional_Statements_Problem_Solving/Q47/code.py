"""To analyze inventory"""

highest_quantity_product = ""
highest_quantity = 0
out_of_stock = 0
critical = 0
low = 0
available = 0

for i in range(8):
    product_name = input("Enter product name: ")
    product_quantity = int(input("Enter product quantity: "))
    if product_quantity > highest_quantity:
        highest_quantity = product_quantity
        highest_quantity_product = product_name

    if product_quantity == 0:
        print("Out of Stock")
        out_of_stock += 1
    elif 5 >= product_quantity >= 1:
        print("Critical")
        critical += 1
    elif 20 >= product_quantity >= 6:
        print("Low")
        low += 1
    elif product_quantity > 20:
        print("Available")
        available += 1

print(f"The product with highest quantity is {highest_quantity_product} with the quantity of {highest_quantity}")
