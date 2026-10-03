"""To print all number from 1 to n which are divisible 2 and 3"""

n = int(input("Enter the ending number: "))
i = 1
while i <= n:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    i += 1
