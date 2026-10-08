"""School Management System"""

user_type = int(input("Enter user type: "))
user_option = int(input("Enter option: "))

match user_type:
    case 1:
        match user_option:
            case 1:
                print("Marks Selected")
            case 2:
                print("Attendance Selected")
            case 3:
                print("Homework Selected")
            case _:
                print("Invalid Option")
    case 2:
        match user_option:
            case 1:
                print("Enter Marks Selected")
            case 2:
                print("Attendance Selected")
            case 3:
                print("Assign Homework Selected")
            case _:
                print("Invalid Option")
    case 3:
        match user_option:
            case 1:
                print("Child Marks Selected")
            case 2:
                print("Child Attendance Selected")
            case 3:
                print("Contact Teacher Selected")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid User")
