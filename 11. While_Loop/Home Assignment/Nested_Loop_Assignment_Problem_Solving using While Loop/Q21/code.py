"""To print 10x10 multiplication grid"""

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1
