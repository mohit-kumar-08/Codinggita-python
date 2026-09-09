a, b, c = map(int,input("enter the three sides of triangle seperated by , : ").split(",")[:3])

if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("Equilateral")
    elif a != b and b != c and c != a:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Invalid triangle")