"""Food Delivery Order Status"""

order_status = input("Enter status: ")

match order_status:
    case "placed":
        print("Your order is placed")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("We are preparing your order.")
    case "out_for_delivery":
        print("Your order is on the way.")
    case "delivered":
        print("Your order is delivered. Enjoy")
    case "cancelled":
        print("Your order is cancelled. Sorry")
    case _:
        print("Invalid status")
