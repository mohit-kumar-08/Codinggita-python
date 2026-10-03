"""To print 1 to 20 in 4 rows"""

number = 1
i = 1
while i <= 4:
    j = 1
    while j <= 5:
        print(number, end=" ")
        number += 1
        j += 1
    print()
    i += 1
