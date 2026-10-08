"""Digital Payment Application"""

payment_type = int(input("Enter Payment Type: "))

match payment_type:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Scan QR")
            case 2:
                print("Enter UPI ID")
            case _:
                print("Invalid Option")
    case 2:
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                print("Credit Card")
            case 2:
                print("Deit Card")
            case _:
                print("Invalid Option")
    case 3:
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                print("Add Money")
            case 2:
                print("Pay Using Wallet")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid method")
