"""To calculate vowels-consonants balance of every word"""

string = input("Enter a string: ").lower()

for i in string.split():
    vowel = 0
    consonant = 0
    for j in range(0, len(i)):
        if i[j] in 'aeiou':
            vowel += 1
        elif 'a' < i[j] <= 'z':
            consonant += 1

    if vowel > consonant:
        print("Vowel Heavy")
    elif vowel < consonant:
        print("Consonant Heavy")
    else:
        print("Balanced")
