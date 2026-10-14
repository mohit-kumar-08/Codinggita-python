"""Search a Word"""

string = input("Enter a sentence: ").split(" ")
target_word = input("Enter the targeted word: ")

for word in string:
    if word == target_word:
        print("Found")
        break
else:
    print("Not Found")