"""Stop at the First Vowel"""

# Code
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)

# Output
# s
# k
# y
# l
