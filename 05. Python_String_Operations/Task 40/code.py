first_name = input()
last_name = input()
city = input()
course = input()
age = input()

#1.
first_name = first_name.strip()
last_name = last_name.strip()
city = city.strip()
course = course.strip()
age = age.strip()

#2.
full_name = first_name + last_name

#3.
print(full_name.title())

#4.
print(full_name.upper())

#5.
print(full_name.lower())

#6.
print(len(full_name))

#7.
print(full_name[0])

#8.
print(full_name[-1])

#9.
print(city, course)

#10.
print(f'{age} years old')

#11.
print("Python" in course)

#12.
course = course.replace("app","web")

#13.
list_of_course = course.split()
print(len(list_of_course))
