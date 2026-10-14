"""Menu Choice"""

print("""
1. View profile
2. Edit profile
3. Settings
4. Exit
""")
option = int(input("select a option: "))

while option < 1 or option > 4:
    print("""
1. View profile
2. Edit profile
3. Settings
4. Exit
""")
    option = int(input("select a option: "))
else:
    print(f"Selected Option {option}")
