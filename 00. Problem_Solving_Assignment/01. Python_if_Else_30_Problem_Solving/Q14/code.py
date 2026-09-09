cost_price = int(input("Enter Cost Price: "))
selling_price = int(input("Enter selling Price: "))

if cost_price > selling_price:
    print(f'Loss = {cost_price - selling_price}')
elif cost_price < selling_price:
    print(f'Profit = {selling_price - cost_price}')
else:
    print("No profit and no loss")