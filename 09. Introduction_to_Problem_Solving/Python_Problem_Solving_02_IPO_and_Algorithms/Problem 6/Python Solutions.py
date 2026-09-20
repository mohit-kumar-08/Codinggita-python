"""To calculate average marks of three subjects"""

marks_1 = int(input("Enter marks of first subject: "))
marks_2 = int(input("Enter marks of second subject: "))
marks_3 = int(input("Enter marks of third subject: "))

average = (marks_1 + marks_2 + marks_3) / 3

if average >= 40:
    print("Pass")
else:
    print("Fail")
