"""Understand Nested Loops"""

# Code
for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")

# Output
# 1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
# Inner loop completed

# 1. The pairs (1,1), (1,3), (2,1) and (2,3) are printed
# 2. Inner loop of iteration 1 and 2 finish without break
# 3. No