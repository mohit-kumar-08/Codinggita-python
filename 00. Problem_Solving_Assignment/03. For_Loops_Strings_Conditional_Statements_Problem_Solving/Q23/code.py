"""To distribute salaries and count average of 8 employees"""

total = 0
junior = 0
mid = 0
senior = 0
executive = 0

for i in range(1, 9):
    salary = int(input(f"Enter salary of {i} employee: "))
    total += salary

    if salary >= 0:
        if salary < 25000:
            junior += 1
            print("Junior")
        elif salary <= 50000:
            mid += 1
            print("Mid")
        elif salary <= 100000:
            senior += 1
            print("Senior")
        else:
            executive += 1
            print("Executive")

print(f"Total juniors are {junior}")
print(f"Total mids are {mid}")
print(f"Total seniors are {senior}")
print(f"Total executives are {executive}")

print(f"Average salary is {total / 8}")
