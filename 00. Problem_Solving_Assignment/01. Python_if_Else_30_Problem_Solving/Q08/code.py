marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks < 40:
    print("Fail")
else:
    print("Pass")