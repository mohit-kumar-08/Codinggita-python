"""Remove all occurrences of a character"""

S = input("Enter a string: ")
C = input("Enter the character to remove: ")
resulted_S = ""

for char in S:
    if char == C:
        continue
    else:
        resulted_S += char
print(resulted_S)
