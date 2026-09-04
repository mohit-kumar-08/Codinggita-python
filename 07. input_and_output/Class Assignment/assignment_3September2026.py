name = str(input("Enter your name: "))
lab = int(input("Enter lab: "))
product_name = str(input("Enter product name: "))
quantity = int(input("Enter product quantity: "))
price = int(input("Enter product price: "))

print(f'''
Name                : {name}
lab                 : {lab}
Product Name        : {product_name}
Product Quantity    : {quantity}
Product Price       : {price}
Total Price         : {quantity*price}
''')
