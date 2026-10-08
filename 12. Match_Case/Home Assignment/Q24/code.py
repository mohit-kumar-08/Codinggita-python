"""Online Exam Portal"""

print("""
1 → Start Exam
2 → View Result
3 → Exit
""")
choice = int(input("Enter choice: "))

match choice:
    case 1:
        age = int(input("Enter age: "))
        if age >= 18:
            print("You can start the exam")
