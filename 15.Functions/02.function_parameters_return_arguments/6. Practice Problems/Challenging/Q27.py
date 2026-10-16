"""to define a function, compare()"""

def compare(a, b):
    if a > b:
        first_value = "A is greater"
    elif b > a:
        first_value = "B is greater"
    else:
        first_value = "Equal"

    if a < 0:
        a *= -1
    if b < 0:
        b *= -1

    second_value = (a, b)

    return first_value, second_value
