"""To print sum of all odd numbers from 1 to n"""

n = int(input("Enter the ending number: "))
i = 1
total = 0
while i <= n:
    if i % 2 != 0:
        total += i
    i += 1
print(total)
