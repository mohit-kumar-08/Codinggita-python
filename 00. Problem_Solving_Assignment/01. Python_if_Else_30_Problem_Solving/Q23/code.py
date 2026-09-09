username = input("Enter Username: ")
password = input("Enter Password: ")

if username == 'admin' and password == 'python123':
    print("Login successful")
elif username != 'admin':
    print("User not found")
elif password != 'python123':
    print("Wrong password")