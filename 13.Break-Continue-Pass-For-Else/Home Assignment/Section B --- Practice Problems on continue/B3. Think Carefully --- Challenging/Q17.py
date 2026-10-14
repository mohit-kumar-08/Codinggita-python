"""Count Non-Vowel Characters"""

string = input("Enter a word: ")
count = 0

for character in string:
    if character in "aeiou":
        continue
    count += 1
print(count)
