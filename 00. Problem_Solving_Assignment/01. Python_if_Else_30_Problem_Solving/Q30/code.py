age = int(input("Enter studnet's age: "))
marks = int(input("Enter student's marks: "))
family_income = int(input("Enter Family annual income: "))
attendance_percentage = int(input("Enter Attendance Percentage: "))

if 18 <= age <= 25 and marks >= 85 and attendance_percentage >= 75 and family_income <= 300000:
    print("Scholarship Approved")
elif age > 25:
    print("Scholarship Rejected")
    print("Reasons: Age above 25")
elif age < 18:
    print("Scholarship Rejected")
    print("Reasons: Age below 18")
elif marks < 85:
    print("Scholarship Rejected")
    print("Reasons: Marks below 85")
elif attendance_percentage < 75:
    print("Scholarship Rejected")
    print("Reasons: Attendance below 75")
elif family_income > 300000:
    print("Scholarship Rejected")
    print("Reasons: Family Income above 300000")