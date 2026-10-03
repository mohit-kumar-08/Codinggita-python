"""To print multiplication grid from 1 to 5"""

i = 1
while i <= 5:
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
    i += 1
