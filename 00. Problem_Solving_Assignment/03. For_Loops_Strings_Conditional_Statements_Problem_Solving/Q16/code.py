"""To find character distribution of given password"""

password = input("Enter your password: ")

uppercase = 0
lowercase = 0
digits = 0
special_characters = 0

for i in password:
    if "a" <= i <= "z":
        lowercase += 1
    elif "A" <= i <= "Z":
        uppercase += 1
    elif "0" <= i <= "9":
        digits += 1
    else:
        special_characters += 1

print(f"Percentage of uppercase characters is, {uppercase / len(password) * 100}%")
print(f"Percentage of lowercase characters is, {lowercase / len(password) * 100}%")
print(f"Percentage of digits characters is, {digits / len(password) * 100}%")
print(f"Percentage of special characters is, {special_characters / len(password) * 100}%")

if uppercase > lowercase and uppercase > digits and uppercase > special_characters:
    print("Uppercase characters dominates the password.")
elif lowercase > uppercase and lowercase > digits and lowercase > special_characters:
    print("Lowercase characters dominates the password.")
elif digits > uppercase and digits > lowercase and digits > special_characters:
    print("Digits dominates the password.")
elif special_characters > uppercase and special_characters > lowercase and special_characters > digits:
    print("Special characters dominates the password.")
