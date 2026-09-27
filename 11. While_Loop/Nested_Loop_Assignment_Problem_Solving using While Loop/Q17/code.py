"""To print row-wise numbers"""

number = 1
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(number, end=" ")
        number += 1
        j += 1
    print()
    i += 1
