"""Employee Portal"""

role = input("Enter role: ")
option = int(input("Enter option: "))

match role:
    case 1:
        match option:
            case 1:
                print("View Profile")
            case 2:
                leave_days = int(input("Enter number of days for leave: "))
                if leave_days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("View Salary")
            case _:
                print("Invalid option")
    case 2:
        match option:
            case 1:
                print("View Team")
            case 2:
                print("Approve Team")
            case 3:
                print("View Reports")
            case _:
                print("Invalid option")
    case _:
        print("Invalid role")
