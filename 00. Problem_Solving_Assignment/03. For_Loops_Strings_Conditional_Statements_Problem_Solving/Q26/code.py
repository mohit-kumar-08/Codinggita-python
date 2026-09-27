"""To print movie rating of 10 movies"""

poor = 0
average = 0
good = 0
excellent = 0
outstanding = 0
total = 0

for i in range(10):
    rating = float(input(f"Enter rating of movie {i + 1}: "))
    total += rating
    if 10 >= rating > 9:
        outstanding += 1
        print("Outstanding")
    elif 9 >= rating > 7:
        excellent += 1
        print("Excellent")
    elif 7 >= rating > 5:
        good += 1
        print("Good")
    elif 5 >= rating > 3:
        average += 1
        print("Average")
    elif 3 >= rating >=0:
        poor += 1
        print("Poor")

print(f"Total Poor => {poor}")
print(f"Total Average => {average}")
print(f"Total Good => {good}")
print(f"Total Excellent => {excellent}")
print(f"Total Outstanding => {outstanding}")
