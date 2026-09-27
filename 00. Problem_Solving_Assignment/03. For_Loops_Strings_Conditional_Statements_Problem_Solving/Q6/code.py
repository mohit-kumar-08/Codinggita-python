"""To count occurence of even and odd count"""

even = 0
odd = 0

for i in range(1, 6):
    number = str(input(f"Enter Number {i}: "))
    if int(number) % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    print("Even occurs more.")
elif even < odd:
    print("Odd occurs more.")
else:
    print("Equal")
