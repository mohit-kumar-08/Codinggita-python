"""University Portal"""

user_type = int(input("Enter user type: "))

match user_type:
    case 1:
        print("""
        1 → View Courses
        2 → View Marks
        3 → View Attendance
        """)
        user_option = int(input("Enter option: "))

        match user_option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid Option")
    case 2:
        print("""
        1 → View Students
        2 → Enter Marks
        3 → View Attendance
        """)
        user_option = int(input("Enter option: "))

        match user_option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Role")