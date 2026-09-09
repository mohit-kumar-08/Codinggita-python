cost_price = int(input("Enter Cost Price: "))
if cost_price <= 0:
    print("Invalid Value")
else:
    selling_price = int(input("Enter selling Price: "))

    if cost_price > selling_price:
        loss = cost_price - selling_price
        print(loss / cost_price * 100)
    elif cost_price < selling_price:
        profit = selling_price - cost_price
        print(profit / cost_price * 100)
    else:
        print("No profit and no loss")