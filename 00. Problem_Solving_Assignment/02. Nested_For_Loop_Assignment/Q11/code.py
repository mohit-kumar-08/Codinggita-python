"""To print alphabet pattern"""

for i in range(5):
    for j in range(0, i + 1):
        print(chr(65 + j), end=" ")
    print()
