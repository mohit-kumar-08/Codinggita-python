age = int(input("Enter you age: "))
marks = int(input("Enter your marks: "))
has_id = input("Do you have a ID?: ")

if has_id == "True":
    has_id = True
else:
    has_id = False

if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")