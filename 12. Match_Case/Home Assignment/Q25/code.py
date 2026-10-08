"""Movie Ticket System"""

print("""
1 → Regular
2 → Premium
3 → VIP
""")
ticket_type = int(input("Enter ticket choice: "))
age = int(input("Enter age: "))
if age < 5:
    print("Free Entry")
else:
    match ticket_type:
        case 1:
            print("Regular")
        case 2:
            print("Premium")
        case 3:
            print("VIP")
        case _:
            print("Invalid Ticket")
