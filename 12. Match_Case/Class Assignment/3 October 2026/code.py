"""Bank Customer Care Toll Free Number Service"""

print("Enter 1 for English")
print("Hindi ke liye 2 dabaaiye")
user_input = int(input("Select Option: "))
print()

match user_input:
    case 1:
        user_input = 9
        while user_input == 9:
            print("Enter 1 for Account Details")
            print("Enter 2 for Emergency Actions")
            print("Enter 3 for Complaint")
            print("Enter 9 for Listening Again")
            user_input = int(input("Select Option: "))
            print()
        match user_input:
            case 1:
                user_input = 9
                while user_input == 9:
                    print("Enter 1 for viewing Account No.")
                    print("Enter 2 for Balance Enquiry")
                    print("Enter 3 for Cheque Services")
                    print("Enter 9 for Listening Again")
                    user_input = int(input("Select Option: "))
                    print()
                match user_input:
                    case 1:
                        print("Your Account No. is 29873874XXXX")
                        print()
                    case 2:
                        print("Your Available Balance is Rs.95,84,245.30")
                        print()
                    case 3:
                        print("Cheque service is Currently Unavailable.")
                        print()
                    case _:
                        print("Invalid Input")
                        print()
            case 2:
                print("We are connecting you with your account Branch Manager.")
                print()
            case 3:
                user_input = 9
                while user_input == 9:
                    print("Enter 1 for Viewing Your Coplaint.")
                    print("Enter 2 for registering a Complaint.")
                    print("Enter 9 for Listening Again")
                    user_input = int(input("Select Option: "))
                    print()
                match user_input:
                    case 1:
                        print("You have not filed any Complaints yet.")
                        print()
                    case 2:
                        print("We are connecting you with a bank employee.")
                        print()
                    case _:
                        print("Invalid Input!")
                        print()
            case _:
                print("Invalid Input!")
                print()
    case 2:
        user_input = 9
        while user_input == 9:
            print("Khaata ki jankari ke liye 1 dabaaiye")
            print("Aapatkaalin harkat ke liye 2 dabaaiye")
            print("Shikayat ke liye 3 dabaaiye")
            print("Dubara sunne ke liye 9 dabaaiye")
            user_input = int(input("Vikalp chuniye!: "))
            print()
        match user_input:
            case 1:
                user_input = 9
                while user_input == 9:
                    print("Khaata sankhiya dekhne ke liye 1 dabaaiye")
                    print("Khaate mai shesh ki jankari ke liye 2 dabaaiye")
                    print("Cheque ki seva ke liye 3 dabaaiye")
                    print("Dubara sunne ke liye 9 dabaaiye")
                    user_input = int(input("Vikalp chuniye!: "))
                    print()
                match user_input:
                    case 1:
                        print("Aapka khaata sankhiya 29873874XXXX hai")
                        print()
                    case 2:
                        print("Aapke khaate mai shesh Rs.95,84,245.30 hai")
                        print()
                    case 3:
                        print("Cheque seva abhi uplabdh nahi hai.")
                        print()
                    case _:
                        print("Aamanya nivesh")
                        print()
            case 2:
                print("Hum aapko Bank manager se jodh rahe hai")
                print()
            case 3:
                user_input = 9
                while user_input == 9:
                    print("Aapni shikayat dekhne ke liye 1 dabaaiye.")
                    print("Shikayat darj karne ke liye 2 dabaaiye")
                    print("Dubara sunne ke liye 9 dabaaiye")
                    user_input = int(input("Vikalp chuniye!"))
                    print()
                match user_input:
                    case 1:
                        print("Aapne koi shikayat darj nahi kari hai.")
                        print()
                    case 2:
                        print("Hum apko bank karamchaari se jodh rahe hai.")
                        print()
                    case _:
                        print("Vikalp chuniye!")
                        print()
            case _:
                print("Vikalp chuniye!")
                print()
    case _:
        print("Invalid Input!")
        print()
