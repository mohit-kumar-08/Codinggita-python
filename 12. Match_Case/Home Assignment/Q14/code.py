"""Customer Support Priority"""

priority_number = int(input("Enter priority number: "))

match priority_number:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
        print("Urgent Priority")
