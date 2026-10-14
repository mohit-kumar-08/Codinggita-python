"""Three Valid Scores"""

score_1 = int(input("Enter score 1: "))
score_2 = int(input("Enter score 2: "))
score_3 = int(input("Enter score 3: "))

while score_1 < 0 or score_1 > 100:
    score_1 = int(input("Enter score 1: "))

while score_2 < 0 or score_2 > 100:
    score_2 = int(input("Enter score 2: "))

while score_3 < 0 or score_3 > 100:
    score_3 = int(input("Enter score 3: "))

print("Total:", score_1 + score_2 + score_3)
print("Average:", (score_1 + score_2 + score_3) / 3)
