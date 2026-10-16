"""to define a function, format_email()"""

def format_function(first, last, uppercase = False):
    full_name = first + " " + last
    upper_full_name = ""
    if uppercase:
        for i in full_name:
            if 97 <= ord(i) <= 122:
                upper_full_name += chr(ord(i) - 32)
            else:
                upper_full_name += i
        return upper_full_name
    else:
        return full_name


