temperature = int(input("Enter temperature unit: "))

if temperature > 35:
    print("Hot")
elif temperature > 25:
    print("Normal")
elif temperature > 15:
    print("Cold")
elif temperature >= 0:
    print("Very Cold")
else:
    print("Freezing")