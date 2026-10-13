"""To assign and sort students according to grades."""

number_of_fail = 0
number_of_pass = 0
number_of_good = 0
number_of_excellent = 0

for i in range(1, 11):
    marks = int(input(f"Enter marks of {i} student: "))
    if 0 <= marks <= 100:
        if marks >= 75:
            print("Excellent")
            number_of_excellent += 1
        elif marks >= 50:
            print("Good")
            number_of_good += 1
        elif marks >= 35:
            print("Pass")
            number_of_pass += 1
        else:
            print("Fail")
            number_of_fail += 1
    else:
        print("Invalid Marks")

print("Number of Excellents are", number_of_excellent)
print("Number of Good are", number_of_good)
print("Number of Pass are", number_of_pass)
print("Number of Fail are", number_of_fail)
