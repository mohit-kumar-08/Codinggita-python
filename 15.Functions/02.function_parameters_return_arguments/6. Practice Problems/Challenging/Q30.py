"""to define a function, order_summary()"""

def order_summary(item, quantity = 1, price = 100, delivery_fee = 40):
    return f"""Item name: {item}
Total cost: {price * quantity + delivery_fee}"""

print(order_summary("eehiwu", 28, 47, delivery_fee = 83))
