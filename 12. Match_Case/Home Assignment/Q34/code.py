"""Gaming Console Menu"""

print("""
1 → Start Game
2 → Load Game
3 → Settings
4 → Exit
""")

option = int(input("Enter option: "))

match option:
    case 1:
        print("Start Game")
    case 2:
        print("Load Game")
    case 3:
        choice = int(input("Enter Choice: "))

        match choice:
            case 1:
                print("Sound")
            case 2:
                print("Graphics")
            case 3:
                print("Controls")
            case _:
                print("Invalid option")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")
