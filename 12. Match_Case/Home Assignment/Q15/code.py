"""Store Discount Category"""

membership_level = int(input("Enter membership level: "))

match membership_level:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
