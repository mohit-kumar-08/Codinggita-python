"""To found the secret word in the string"""

string = input("Enter the sentence: ")
secret_word = input("Enter the secret word: ")

if string.find(secret_word) == -1:
    print("Secret word not found")
else:
    print(f"Starting position of secret word in sentence is {string.find(secret_word) + 1}.")
    print(f"The secret word occurs {string.count(secret_word)} times in the sentence.")