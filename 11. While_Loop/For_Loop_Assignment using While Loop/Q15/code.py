"""To count even numbers from 1 to n"""

n = int(input("Enter the ending number: "))
i = 1
count = 0
while i <= n:
    if i % 2 == 0:
        count += 1
    i += 1
print(count)
