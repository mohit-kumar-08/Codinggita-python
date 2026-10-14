"""Stop at a Target Number"""

limit = int(input("Enter a limit: "))

for i in range(1, limit + 1):
    if i == 7:
        break
    print(i, end=" ")
