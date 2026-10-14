"""Temperature Range"""

temperature = int(input("Enter temperature between -20 and 45: "))

while temperature < -20 or temperature > 45:
    temperature = int(input("Enter temperature between -20 and 45: "))
