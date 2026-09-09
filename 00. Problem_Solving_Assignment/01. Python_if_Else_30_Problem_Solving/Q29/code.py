num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if num_1 < num_2:
    if num_2 < num_3:
        print(num_2)
    else:
        print(num_3)
elif num_2 < num_3:
    if num_3 < num_1:
        print(num_3)
    else:
        print(num_1)
elif num_3 < num_1:
    if num_1 < num_2:
        print(num_1)
    else:
        print(num_2)