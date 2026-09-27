"""To print odd number pattern"""

i = 1
while i <= 5:
    row = ""
    j = 1
    while j <= i * 2:
        if j % 2 != 0:
            row += str(j) + " "
        j += 1
    print(row)
    i += 1
