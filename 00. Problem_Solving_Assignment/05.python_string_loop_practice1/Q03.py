"""Check whether both halves are palindromes"""

length_of_string = int(input("Enter the length of the string: "))
string = input("Enter the string: ")

if length_of_string % 2 == 0:
    half_length_of_string = int(len(string) / 2)
    substring_1 = string[: half_length_of_string]
    substring_2 = string[half_length_of_string:]

    for i in range(len(substring_1)):
        for j in range(len(substring_1) - 1, -1, -1):
            if substring_1[i] == substring_1[j]:
                substring_1_is_palindrome = True
            else:
                substring_1_is_palindrome = False

    for i in range(len(substring_2)):
        for j in range(len(substring_2) - 1, -1, -1):
            if substring_2[i] == substring_2[j]:
                substring_2_is_palindrome = True
            else:
                substring_2_is_palindrome = False

    if substring_1_is_palindrome and substring_2_is_palindrome:
        print('yes')
    else:
        print("no")
else:
    print("no")
