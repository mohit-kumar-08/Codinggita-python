a, b, c = map(int,input("enter the three sides of triangle seperated by , : ").split(",")[:3])

if a + b > c and b + c > a and c + a > b:
    print("Valid triangle")
else:
    print("Invalid triangle")