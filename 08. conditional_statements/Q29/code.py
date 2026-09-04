is_student = bool(input("Are you a student?: "))
has_id = bool(input("Do you have id?: "))
has_ticket = bool(input("Do you have the ticket?: "))

if is_student == "True":
    is_student = True
else:
    is_student = False

if has_id == "True":
    has_id = True
else:
    has_id = False

if has_student == "True":
    has_student = True
else:
    has_student = False

if is_student is True and has_id is True and has_ticket is True:
    print("Allowed")