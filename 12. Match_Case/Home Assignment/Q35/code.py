"""Restaurant Ordering System"""

category = int(input("Enter category: "))

match category:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Soup")
            case 2:
                print("Spring Roll")
            case 3:
                print("Garlic Bread")
            case _:
                print("Invalid Option")
    case 2:
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                print("Pizza")
            case 2:
                print("Pasta")
            case 3:
                print("Biryani")
            case _:
                print("Invalid Option")
    case 3:
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                print("Ice Cream")
            case 2:
                print("Cake")
            case 3:
                print("Gulab jamun")
            case _:
                print("Invalid Option")
    case 4:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Coffee")
            case 2:
                print("Tea")
            case 3:
                print("Juice")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Category")
