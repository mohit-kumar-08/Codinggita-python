"""Does else Run?"""

### Case A

# Code
for x in range(3):
    continue
else:
    print("A")

# Output
# A




### Case B

# Code
for x in range(3):
    break
else:
    print("B")

# Output
#




### Case C

# Code
for x in range(0):
    print(x)
else:
    print("C")

# Output
# C