"""to find length of each aplhabet in a given string"""

string = input("Enter a string: ")
counted_character = ""
for char in string:
    count = 0
    if char not in counted_character:
        counted_character += char
        for i in string:
            if i == char:
                count += 1
        print(f"{char} {count}")

#Completed on 24 October 2026
