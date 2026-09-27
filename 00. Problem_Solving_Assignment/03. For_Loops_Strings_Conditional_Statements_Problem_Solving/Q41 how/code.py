"""To analyze attendance of 7 students for 5 days"""

for i in range(7):
    total_attendance = 0
    for j in range(5):
        attendance = input(f"Enter student {i + 1}'s attendance of day {j + 1} (P/A): ")

        if attendance == "P":
            total_attendance += 1

    print(f"Total attendance of student {i + 1} is {total_attendance} out of 5")

    attendance_percent = total_attendance * 100 / 5

    if attendance_percent >= 90:
        print("Excellent")
    elif attendance_percent >= 75:
        print("Good")
    else:
        print("Warning")
