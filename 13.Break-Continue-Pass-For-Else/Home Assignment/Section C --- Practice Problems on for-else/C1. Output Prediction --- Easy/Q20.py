"""Completion After break"""

# Code
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")

# Output
# 1
# 2
# Outside loop
