"""Find the first position of a character"""

S = input("Enter a string: ")
C = input("Enter the character to find: ")

for i in range(len(S)):
    if S[i] == C:
        print(i)
        break
else:
    print(-1)
