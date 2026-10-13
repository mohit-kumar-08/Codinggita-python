"""Age Group"""

age = int(input("Enter your age: "))
if 0 <= age <= 12:
    print("child")
elif 13 <= age <= 19:
    print("teenager")
else:
    print("adult")
