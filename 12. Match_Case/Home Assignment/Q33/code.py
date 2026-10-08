"""Travel Booking System"""

transport = int(input("Enter transport: "))
travel_option = int(input("Enter option: "))

match transport:
    case 1:
        match travel_option:
            case 1:
                print("Economy Flight Selected")
            case 2:
                print("Business Flight Selected")
            case _:
                print("Invalid Option")
    case 2:
        match travel_option:
            case 1:
                print("Sleeper Train Selected")
            case 2:
                print("AC Train Selected")
            case _:
                print("Invalid Option")
    case 3:
        match travel_option:
            case 1:
                print("Ordinary Bus Selected")
            case 2:
                print("Volvo Bus Selected")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid transport.")
