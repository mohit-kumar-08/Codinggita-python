name_1 = input("Enter Name of person 1: ")
age_1 = int(input("Enter age of person 1: "))

name_2 = input("Enter Name of person 2: ")
age_2 = int(input("Enter age of person 2: "))

name_3 = input("Enter Name of person 3: ")
age_3 = int(input("Enter age of person 3: "))

if age_1 == age_2 and age_2 == age_3:
    print(f'{name_1}, {name_2} and {name_3} all three are young')
elif age_1 < age_2 and age_1 < age_3:
    print(f'{name_1} is the youngest')
elif age_2 < age_1 and age_2 < age_3:
    print(f'{name_2} is the youngest')
elif age_3 < age_1 and age_3 < age_2:
    print(f'{name_3} is the youngest')
elif age_1 == age_2:
    if age_1 < age_3:
        print(f'{name_1} and {name_2} are the youngest')
    else:
        print(f'{name_3} is the youngest')
elif age_1 == age_3:
    if age_1 < age_2:
        print(f'{name_1} and {name_3} are the youngest')
    else:
        print(f'{name_2} is the youngest')
elif age_2 == age_3:
    if age_2 < age_1:
        print(f'{name_2} and {name_3} are the youngest')
    else:
        print(f'{name_1} is the youngest')
