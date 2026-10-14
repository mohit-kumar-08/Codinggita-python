"""Compare pass and continue"""

### Program A

# Code
for i in range(1, 5):
    if i == 3:
        pass
    print(i)

# Output
# 1
# 2
# 3
# 4



### Program B
for i in range(1, 5):
    if i == 3:
        continue
    print(i)

# Output
# 1
# 2
# 4
