"""Food Ordering System"""

print('''
1 → Pizza
2 → Burger
3 → Pasta
4 → Sandwich
''')

customer_choice = int(input("Choose your Order: "))

match customer_choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")
    case 4:
        print("You selected Sandwich")
    case _:
        print("Invalid Menu Choice")
