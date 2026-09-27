"""to print U shape star pattern"""

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == n or i == n:
            print("*", end=" ")
        elif n % 2 == 0:
            if i == n // 2 and j == n // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")   
        elif n % 2 != 0:
            if i == n // 2 + 1 and j == n // 2 + 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print(" ", end=" ")
    print()
