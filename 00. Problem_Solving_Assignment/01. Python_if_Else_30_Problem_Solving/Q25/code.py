marks_1 = int(input("Enter Marks of subject 1: "))
marks_2 = int(input("Enter Marks of subject 2: "))
marks_3 = int(input("Enter Marks of subject 3: "))

if 0 <= marks_1 <= 100 and 0 <= marks_2 <= 100 and 0<= marks_3 <=100:
    if marks_1 < 35 or marks_2 < 35 or marks_3 < 35:
        print("Fail")
    else:
        average = (marks_1 + marks_2 + marks_3) / 3
        if average >= 75:
            print("Distinction")
        elif average >= 60:
            print("First Class")
        elif average >= 50:
            print("Second Class")
        else:
            print("Pass")
else:
    print("Enter Valid marks")