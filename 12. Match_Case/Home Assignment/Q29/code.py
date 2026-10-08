"""Library Management System"""

print("""
1 → Search Book
2 → Issue Book
3 → Return Book
4 → View Issued Books
5 → Exit
""")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Search Book Processed")
    case 2:
        print("Issue Book Processed")
    case 3:
        print("Return Book Processed")
    case 4:
        print("View Issued Books Processed")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")
