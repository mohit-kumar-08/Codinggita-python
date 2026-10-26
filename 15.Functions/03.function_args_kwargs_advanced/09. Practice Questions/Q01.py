"""to define a function with *args, multiply_all()"""

def multiply_all(*args):
    count_of_number = 0
    supplied_number = 1
    for number in args:
        count_of_number += 1
        supplied_number *= number
    if count_of_number == 0:
        supplied_number = 0
    return supplied_number

