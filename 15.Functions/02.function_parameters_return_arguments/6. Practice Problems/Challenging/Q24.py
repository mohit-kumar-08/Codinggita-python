"""to define a function, apply_discount()"""

def apply_function(price, discount = 0):
    final_price = price - price * discount / 100
    return final_price
