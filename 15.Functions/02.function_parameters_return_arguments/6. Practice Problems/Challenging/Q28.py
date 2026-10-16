"""to define a function, convert_temperature()"""

def convert_temperature(value, scale = "C"):
    if scale == "C":
        resulted_value = (value * 9 / 5) + 32
    else:
        resulted_value = (value - 32) * 5 / 9

    return resulted_value
