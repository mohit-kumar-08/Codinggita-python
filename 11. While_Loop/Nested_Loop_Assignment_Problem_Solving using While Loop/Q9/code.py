"""To print multiplication grid"""

i = 1
while i <= 3:
    j = 1
    while j <= 5:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1
