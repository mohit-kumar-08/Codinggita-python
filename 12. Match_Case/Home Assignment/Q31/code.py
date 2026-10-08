"""Banking Application with Nested Menu"""

banking_type = int(input("Enter banking type: "))
banking_option = int(input("Enter option: "))

match banking_type:
    case 1:
        match banking_option:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Option")
    case 2:
        match banking_option:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Business Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")
    case _:
        print('Invalid Banking Type')
