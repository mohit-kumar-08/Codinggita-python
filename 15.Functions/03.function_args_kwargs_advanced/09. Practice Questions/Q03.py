"""to define a function using / and *, make_message()"""

def make_message(name, /, *, greeting="Hello"):
    message = greeting + " " + name
    return message
