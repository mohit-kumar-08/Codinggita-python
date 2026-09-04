name = str(input("Enter student's name: "))
age = int(input("Enter student's age: "))
height = float(input("Enter student's height: "))
city = str(input("Enter student's city: "))
print(f'''
    Student Information
Student's Name      : {name}
Student's Age       : {age}
Student's Height    : {height:.2f}
Student's City      : {city}''')