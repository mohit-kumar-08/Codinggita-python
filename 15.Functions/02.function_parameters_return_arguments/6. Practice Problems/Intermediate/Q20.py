"""to define a function, bill()"""

def bill(item, quantity = 1, price = 100):
    return f"""Item Name: {item}
Item Price: {quantity * price}"""

print(bill("joewu", 83, 200))
print(bill(quantity = 857, price = 500, item = "efbhjs"))
