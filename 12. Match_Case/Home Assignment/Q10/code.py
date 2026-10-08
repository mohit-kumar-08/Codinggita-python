"""Payment Method"""

payment_method = input("Enter payment method: ")

match payment_method:
    case "upi":
        print("UPI Payemnt Selected")
    case "card":
        print("Card Payemnt Selected")
    case "cash":
        print("Cash Payemnt Selected")
    case "wallet":
        print("Wallet Payemnt Selected")
    case _:
        print("Invalid Payment Method")
