"""To validate product code"""

code = input("Enther the product code: ")

code_status = True
char_count = 0

for i in code[:3]:
    if 65 <= ord(i) <= 90:
        char_count += 1
    else:
        code_status = False

for i in code[3:]:
    if 48 <= ord(i) <= 57:
        char_count += 1
    else:
        code_status = False

if char_count == 8 and code_status is True:
    print("Valid Product Code")
else:
    print("Invalid Product Code")
