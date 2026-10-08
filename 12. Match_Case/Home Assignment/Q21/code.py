"""Temperature Converter"""

choice = int(input("Enter choice: "))
temperature = int(input("Enter temperature: "))

match choice:
    case 1:
        print(f"Temperature = {(temperature * 1.8) + 32} F")
    case 2:
        print(f"Temperature = {(temperature - 32) / 1.8} C")
    case _:
        print("Invalid Choice")
