"""Banking Service Selection"""

print("""
1 → Account Balance
2 → Mini Statement
3 → Fund Transfer
4 → Bill Payment
5 → Customer Support
""")

service = int(input("Enter service: "))

match service:
    case 1:
        print("Opening Account Balance")
    case 2:
        print("Opening Mini Statement")
    case 3:
        print("Opening Fund Transfer")
    case 4:
        print("Opening Bill Payemnt")
    case 5:
        print("Opening Customer Support")
    case _:
        print("Invalid Service")