"""To print decreasing star pattern"""

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or j == 1:
            print('*', end=" ")
        elif i == 2 and j != 5:
            print('*', end=" ")
        elif j == 2 and i != 5:
            print('*', end=" ")
        elif i == 3 and j == 3:
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print()
