"""To find occurence of character in a string"""

string = input("Enter a string: ")
count = 0
for i in string:
    # count = 0
    if i in string:
        count += 1
    if count == 2:
        print(f"{i} is Duplicate")
    elif 3 <= count <= 4:
        print(f"{i} is Repeated")
    elif count > 4:
        print(f"{i} is Highly Repeated")
