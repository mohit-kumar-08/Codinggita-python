"""To print multiplication table from 1 to 5"""

i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(j * i, end="\t")
        j += 1
    print()
    i += 1
