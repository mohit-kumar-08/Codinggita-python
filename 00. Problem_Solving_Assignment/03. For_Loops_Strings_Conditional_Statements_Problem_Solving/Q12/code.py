"""To count vowels and consonants in a string"""

vowel = 0
consonant = 0

string = input("Enter a string: ").lower()

for i in string:
    if i in 'aeiou':
        vowel += 1
    elif 'a' < i <= 'z':
        consonant += 1

if vowel > consonant:
    print("Vowels Win")
elif vowel < consonant:
    print("Consonants Win")
else:
    print("Draw")
