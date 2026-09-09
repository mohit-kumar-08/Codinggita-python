electricity_unit = int(input("Enter your electricity bill: "))

if electricity_unit <= 100:
    print(electricity_unit * 5)
elif electricity_unit <= 200:
    electricity_unit -= 100
    print(electricity_unit * 7 + 500)
else:
    electricity_unit -= 200
    print(electricity_unit * 10 + 500 + 700)