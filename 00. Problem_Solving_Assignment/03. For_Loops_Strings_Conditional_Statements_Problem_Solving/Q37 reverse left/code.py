"""To generate a character pyramid"""

word = input("Enter a word: ")

for i in word:
    for j in range(0, word.index(i) + 1):
        print(word[j], end="")
    print()

