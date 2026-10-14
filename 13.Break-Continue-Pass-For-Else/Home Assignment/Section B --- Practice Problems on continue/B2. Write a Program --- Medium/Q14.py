"""Print Only Passing Marks"""

list_of_marks = map(int, input("Enter marks: ").split(" "))

for marks in list_of_marks:
    if marks < 40:
        continue
    print(marks, end=" ")
