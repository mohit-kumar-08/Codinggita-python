"""Completion After continue"""

# Code
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

# Output
# 1
# 3
# 4
# Completed
