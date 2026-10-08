"""Railway Ticket System"""

print("""
1 → Book Ticket
2 → Cancel Ticket
3 → Check PNR
4 → Train Schedule
5 → Exit
""")

action = int(input("Enter action: "))

match action:
    case 1:
        print("Book Ticket")
    case 2:
        print("Cancel Ticket")
    case 3:
        print("Check PNR")
    case 4:
        print("Train Schedule")
    case 5:
        print("Exit")
    case _:
        print("Invalid Action")
