#1. 10 + 5 * 2
print("Expected Result: 20")
#Python first evaluated * operator, then + operator
print(10 + 5 * 2)

#2. 20 - 4 / 2
print("Expected Result: 18")
#Python first evaluated / operator, then - operator
print(20 - 4 / 2)

#3. 10 + 20 / 5 * 2
print("Expected Result: 18")
#Python first evaluated / operator, then * operator and then + operator
print(10 + 20 / 5 * 2)

#4. 2 + 3 * 4 ** 2
print("Expected Result: 50")
#Python first evaluated ** operator, then * operator and then + operator
print(2 + 3 * 4 ** 2)

#5. 100 - 20 // 5
print("Expected Result: 96")
#Python first evaluated // operator and then - operator
print(100 - 20 // 5)