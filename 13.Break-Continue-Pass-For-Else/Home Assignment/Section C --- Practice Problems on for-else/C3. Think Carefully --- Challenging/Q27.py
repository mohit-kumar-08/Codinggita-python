"""Find the First Repeated Character"""

string = input("Enter a string: ")

for i in string:
    count = 0
    for j in string:
        if j == i:
            count += 1
    if count > 1:
        print(i)
        break
else:
    print("No repeated character")
