# Q1.
string = input("Enter a string: ")
previous_char = ""
resulted_string = ""
count_of_char = 0
while string != "":
    if string[0] == previous_char:
        count_of_char += 1
        string = string[1:]
        if string == "":
            resulted_string += str(count_of_char)
    else:
        if count_of_char != 0:
            resulted_string += str(count_of_char)
        resulted_string += string[0]
        previous_char = string[0]
        count_of_char = 0
print(resulted_string)



# Q2.
string = input("Enter a string: ")
result = ""
for i in range(0, len(string)):
    if i % 2 == 0:
        result += string[i] * int(string[i + 1])
print(result)


# Q3. 
def half_palindrome_checker(string):
    """Checking length of the string"""
    if len(string) % 2 != 0:
        return "Give a string with even length."
    else:
        """creating two substring of equal length from the main string"""
        half_length_of_string = int(len(string) / 2)
        substring_1 = string[: half_length_of_string]
        substring_2 = string[half_length_of_string:]

        """checking palindrome of first substring"""
        for i in range(len(substring_1)):
            for j in range(len(substring_1) - 1, -1, -1):
                if substring_1[i] == substring_1[j]:
                    substring_1_is_palindrome = True
                else:
                    substring_1_is_palindrome = False

        """checking palindrome of second substring"""
        for i in range(len(substring_2)):
            for j in range(len(substring_2) - 1, -1, -1):
                if substring_2[i] == substring_2[j]:
                    substring_2_is_palindrome = True
                else:
                    substring_2_is_palindrome = False

        """Output: if the string is half palindrome or not"""
        if substring_1_is_palindrome and substring_2_is_palindrome:
            return 'The given string is halfly palindrome'
        else:
            return"The given string is not halfly palindrome"
