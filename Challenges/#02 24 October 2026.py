"""to find position of a substring in a given string, without using any built-in function"""

string = input("Enter the sentence: ")
substring = input("Enter the word to find: ")

length_of_string = 0
for char in string:
    length_of_string += 1

length_of_substring = 0
for char in substring:
    length_of_substring += 1

for i in range(length_of_string):
    for j in range(length_of_substring):
        copy_of_substring = substring
        if string[i] == substring[j]:
            position_of_substring = i
            while copy_of_substring != "":
                if string[i] == copy_of_substring[0]:
                    copy_of_substring = copy_of_substring[1:]
                    i += 1
                else:
                    position_of_substring = -1
                    break
            else:
                print()
                print(f"The word is at index {position_of_substring} in the sentence.")
                print()
                break
            break
        break

if position_of_substring == -1:
    print()
    print("The word is not in the sentence.")
    print()

#Completed on 27 October 2026
