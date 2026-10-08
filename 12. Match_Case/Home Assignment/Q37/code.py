"""Online Learning Platform"""

category = int(input("Enter category: "))
option = int(input("Enter option: "))

match category:
    case 1:
        match option:
            case 1:
                print("Python")
            case 2:
                print("Java")
            case 3:
                print("C++")
            case _:
                print("Invalid option")
    case 2:
        match option:
            case 1:
                print("Algebra")
            case 2:
                print("Calculus")
            case 3:
                print("Statistics")
            case _:
                print("Invalid option")
    case 3:
        match option:
            case 1:
                print("English")
            case 2:
                print("Presentation")
            case 3:
                print("Interview Skills")
            case _:
                print("Invalid option")
    case _:
        print("Invalid category")
