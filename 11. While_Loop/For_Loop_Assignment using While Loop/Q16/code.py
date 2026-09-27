"""To print sum of all number from 1 to n"""

n = int(input("Enter the ending number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(total)
