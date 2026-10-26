"""to call a parameter by  unpacking a dictionary"""

def intro(name, age):
    return f"""
Name: {name}
Age: {age}
"""

person = {"name": "Ravi", "age": 21}
print(intro(**person))
