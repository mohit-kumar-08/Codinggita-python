"""To classify each number in a pyramid"""

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(1, 2*i):
        a = ""
        if j % 3 == 0 and j % 5 == 0:
            a =  "F"
        elif j % 3 == 0:
            a = "T"
        elif j % 2 == 0:
            a = "E"
        else:
            a = "O"

        print(a, end="")
    print()
