"""To print reverse number pattern"""

m = 0

for i in range(5):
    for j in range(5, m, -1):
        print(j, end=" ")
    print()
    m += 1
