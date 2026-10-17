"""to print factorial using recursion"""

count = 1
result = 1
def factorial(number):
    
    global count
    global result

    if count == number:
        result *= number
        return result

    result *= count
    count += 1

    return factorial(number)

print(factorial(5))
