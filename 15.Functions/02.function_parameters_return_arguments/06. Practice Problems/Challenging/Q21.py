"""to define a function, analyze_number()"""

def analyze_number(number):
    if number < 0:
        absolute_value = number * -1
    else:
        absolute_value = number

    if number % 2 == 0:
        is_even = True
    else:
        is_even = False

    count = 0
    for i in str(absolute_value):
        if 0 <= int(i) <= 9:
            count += 1

    return f"""Absolute Value: {absolute_value}
Is number Even: {is_even}
Number of digits in the number: {count}"""

print(analyze_number(-45))
