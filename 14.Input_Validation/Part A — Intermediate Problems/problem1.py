"""Valid Marks"""

marks = 101
while marks > 100 or marks < 0:
    marks = int(input("Enter marks: "))
else:
    print("Accepted marks:", marks)
