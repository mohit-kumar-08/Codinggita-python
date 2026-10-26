"""to define a function with **kwargs, print_profile()"""

def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
