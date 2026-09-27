"""To generate password from text"""

text = input("Enter a text: ")
password = ""

for i in text:
    if i.lower() in 'aeiou':
        password += '@'
    elif 97 <= ord(i.lower()) <= 122:
        password += i.lower()
    elif  ord(i) == 32:
        password += "_"
    elif 48 <= ord(i) <= 57:
        password += "#"
    else:
        password += "!"

print(password)
