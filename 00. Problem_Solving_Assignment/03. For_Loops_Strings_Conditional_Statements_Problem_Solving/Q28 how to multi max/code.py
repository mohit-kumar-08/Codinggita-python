"""To find number with maximum even digits"""
high_even_digit = 0
high_even_number = ""
for i in range(10):
    even_digit = 0
    odd_digit = 0
    number = str(int(input(f"Enter number {i + 1}: ")))

    for digit in number:
        if int(digit) % 2 == 0:
            even_digit += 1
        else:
            odd_digit += 1
    if even_digit > high_even_digit:
        high_even_digit = even_digit
        high_even_number = number

    print(f"No. of even digits: {even_digit}")
    print(f"No. of odd digits: {odd_digit}")
print(f"Number having highest no. of even digits: {high_even_number}")
