"""Find the First Divisor"""

n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")
