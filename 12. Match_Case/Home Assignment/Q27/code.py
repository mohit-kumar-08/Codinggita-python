"""Hospital Department Selection"""

print("""
1 → General Medicine
2 → Cardiology
3 → Orthopedics
4 → Pediatrics
5 → Emergency
""")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("General Medicine")
    case 2:
        print("Cardiology")
    case 3:
        print("Orthopedics")
    case 4:
        print("Pediatrics")
    case 5:
        print("Emergency")
    case _:
        print("Invalid Department")
