"""To print number box pattern"""

n = int(input("Enter teh size of box: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n:
            print('*', end="")
        elif j == 1 or j == n:
            print('*', end="")
        elif i % 2 == 0 and j % 2 == 0:
            print("E", end="")
        else:
            print("O", end="")
    print()
