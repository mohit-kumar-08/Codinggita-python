"""to call a parameter by  unpacking a list"""

def addition(a, b, c):
    return a + b + c

values = [4, 5, 6]
print(addition(*values))
