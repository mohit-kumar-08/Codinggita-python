is_closed = input("Is it closed?: ")
is_closed = bool(is_closed)

if is_closed == "True":
    is_closed = True
else:
    is_closed = False

if is_closed is not True:
    print("Open")