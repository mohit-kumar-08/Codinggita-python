"""To print odd number pattern"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print()
