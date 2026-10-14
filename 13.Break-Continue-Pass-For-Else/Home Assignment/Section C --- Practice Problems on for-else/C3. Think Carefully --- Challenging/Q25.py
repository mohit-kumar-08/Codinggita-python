"""Trace the else"""

# Code
values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")

# Output
# All are even
