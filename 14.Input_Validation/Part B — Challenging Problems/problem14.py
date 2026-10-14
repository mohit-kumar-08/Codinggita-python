"""Marks and Result"""

marks = -1

while marks < 0 or marks > 100:
    marks = int(input("Enter marks: "))
else:
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 35:
        print("Pass")
    else:
        print("Fail")
