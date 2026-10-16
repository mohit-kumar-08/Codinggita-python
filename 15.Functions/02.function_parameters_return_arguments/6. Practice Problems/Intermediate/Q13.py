"""to define a function, classify_number(number)"""

def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(classify_number(94))
