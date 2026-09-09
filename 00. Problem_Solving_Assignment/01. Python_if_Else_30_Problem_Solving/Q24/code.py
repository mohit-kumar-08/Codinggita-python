purchase_amount = int(input("Enter purchase amount: "))

if purchase_amount < 500:
    discount = 0
elif purchase_amount >= 5000:
    discount = 20
elif purchase_amount >= 2000:
    discount = 15
elif purchase_amount >= 1000:
    discount = 10
elif purchase_amount >= 500:
    discount = 5

print(f"""
Discount: {discount}%
Discount amount: ₹{purchase_amount * discount / 100}
Final amount: ₹{purchase_amount - (purchase_amount * discount / 100)}""")