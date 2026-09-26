"""To print a 10x10 multiplication grid"""

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
