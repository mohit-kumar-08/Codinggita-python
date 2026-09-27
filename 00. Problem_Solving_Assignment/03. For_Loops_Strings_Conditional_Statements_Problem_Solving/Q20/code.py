"""To analyze each number in a grid"""

n = int(input("Enter a number for grid: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        number = i * j
        if number % 5 == 0:
            print("F", end=" ")
        elif number % 2 == 0:
            print("E", end=" ")
        else:
            print("O", end=" ")
    print()
