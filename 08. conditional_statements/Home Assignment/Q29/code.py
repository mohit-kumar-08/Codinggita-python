print("Answer in Yes/No")
is_student = input("Are you a student?: ")
has_id = input("Do you have id?: ")
has_ticket = input("Do you have the ticket?: ")

if is_student == "Yes":
    is_student = True
elif is_student == "No":
    is_student = False

if has_id == "Yes":
    has_id = True
elif has_id == "No":
    has_id = False

if has_ticket == "Yes":
    has_ticket = True
elif has_ticket == "No":
    has_ticket = False

if is_student is True and has_id is True and has_ticket is True:
    print("Allowed")