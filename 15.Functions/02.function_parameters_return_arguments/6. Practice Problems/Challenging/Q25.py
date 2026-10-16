"""to define a function, calculate_pay()"""

def calculate_pay(hours, rate = 200, bonus = 0):
    return hours * rate + bonus

print(calculate_pay(24, bonus = 82, rate = 506))
print(calculate_pay(24, 842, bonus = 506))
