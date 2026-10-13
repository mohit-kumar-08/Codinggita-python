"""To print increasing star pattern"""

for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or i == 5:
            print('*', end=" ")
        elif j == 2 and i != 1:
            print('*', end=" ")
        elif i == 4 and j != 5:
            print('*', end=" ")
        elif i == 3 and j == 3:
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print()
