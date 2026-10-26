"""to define a function, calculate_status()"""

def calculate_status(a, b, c):
    sum_of_three = a + b + c

    if a > b and a > c:
        largest = a
        if b > c:
            smallest = c
        else:
            smallest = b
    elif b > a and b > c:
        largest = b
        if a > c:
            smallest = c
        else:
            smallest = a
    elif c > a and c > b:
        largest = c
        if a > b:
            smallest = b
        else:
            smallest = a
    elif a == b and a == c:
        largest = a
        smallest = a

    return f"""Largest Number: {largest}
Smallest Number: {smallest}
Sum of Three: {sum_of_three}"""
