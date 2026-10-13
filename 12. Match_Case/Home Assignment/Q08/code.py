"""Movie Ticket Booking"""

print("""
1 → Morning Show
2 → Afternoon Show
3 → Evening Show
4 → Night Show
""")

show = int(input("Enter show: "))

match show:
    case 1:
        print("Morning Show Selected")
    case 2:
        print("Afternoon Show Selected")
    case 3:
        print("Evening Show Selected")
    case 4:
        print("Night Show Selected")
    case _:
        print("Invalid Show")