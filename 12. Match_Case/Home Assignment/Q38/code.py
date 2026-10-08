"""Smart Vehicle Dashboard"""

category = int(input("Enter category: "))
option = int(input("Enter option: "))

match category:
    case 1:
        match option:
            case 1:
                print("Start")
            case 2:
                print("Stop")
            case _:
                print("Invalid Option")
    case 2:
        match option:
            case 1:
                print("Headlights")
            case 2:
                print("Indicators")
            case 3:
                print("Hazard Lights")
            case _:
                print("Invalid Option")
    case 3:
        match option:
            case 1:
                print("Play")
            case 2:
                print("Pause")
            case 3:
                print("Next")
            case 4:
                print("Previous")
            case _:
                print("Invalid Option")
    case 4:
        match option:
            case 1:
                print("Start Navigation")
            case 2:
                print("Stop Navigation")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Category")
