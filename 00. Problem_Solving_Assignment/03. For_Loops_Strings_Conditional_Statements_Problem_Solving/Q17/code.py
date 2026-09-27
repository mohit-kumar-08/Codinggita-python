"""To analyze student's name and marks"""

max_marks = 0

for i in range(1, 6):
    grade = ""
    vowels = 0
    consonants = 0
    name = input(f"Enter {i} student's name: ").lower()
    marks = int(input(f"Enter {name}'s marks: "))
    if marks > max_marks:
        max_marks = marks

    if 0 <= marks <= 100:
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        elif marks >= 50:
            grade = "E"
        else:
            grade = "F"

    for character in name:
        if character in 'aeiou':
            vowels += 1
        elif 'a' < character <= 'z':
            consonants += 1

    print(f"Grade of {name} is {grade}")
    print(f"vowels in name of {name} is {vowels}")
    print(f"Total characters in name of {name} is {len(name)}")

    if vowels > consonants:
        print(f"Vowels are more in name of {name}")
    elif consonants > vowels:
        print(f"Consonants are more in name of {name}")
    else:
        print(f"There are equal no. of vowels and consonants in the name of {name}")

print(f"Maximum marks of a student is {max_marks}")
