print("Answer in yes or no")
is_student = str(input("Are you a Student: "))


if is_student == "yes":
    attendance = int(input("Whats your attendance percentage: "))
    fees_status = str(input("Is your fees complete: "))
    if fees_status == "yes":
        if attendance >= 75:
            print("You are eligible for exams")
        if attendance < 75:
            print("You are not eligible for exams")
    if fees_status == "no":
        print("You are not eligible for exams")
    if fees_status != "yes" and fees_status != "no":
        print("Enter a Valid Input.")
if is_student == "no":
    print("Exams are only for Students.")
if is_student != "yes" and is_student != "no":
    print("Enter a Valid Input.")


