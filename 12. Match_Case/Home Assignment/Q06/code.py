"""Online Shopping Menu"""

print("""
1 → Electronics
2 → Clothing
3 → Books
4 → Grocery
5 → Exit
""")

category = int(input("Enter category: "))

match category:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid Category")
