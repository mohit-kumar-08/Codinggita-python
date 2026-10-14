"""break Only Exits the Inner Loop"""

# Code
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

# Output
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2
