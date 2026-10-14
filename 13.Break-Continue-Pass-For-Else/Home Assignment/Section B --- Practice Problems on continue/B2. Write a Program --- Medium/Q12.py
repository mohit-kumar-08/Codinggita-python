"""Print Numbers That Are Not Multiples of 3"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i)
