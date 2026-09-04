age = int(input("Enter your age: "))
has_id = input("Do you have ID?: ")

if has_id == "True":
    has_id = True
else:
    has_id = False

if age >= 18 and has_id is True:
    print("Allowed")