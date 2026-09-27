"""To calculate electricity bill"""

for i in range(1, 7):
    total_bill = 0
    bill_range = ""
    units = int(input(f"Enter electricity units of {i} person"))

    if units <= 100:
        total_bill = units * 5
    elif units <= 200:
        units = units - 100
        total_bill = (units * 7) + 500
    elif units <= 400:
        units = units - 200
        total_bill = (units * 10) + 1200
    else:
        units = units - 400
        total_bill = (units * 15) + 2200

    if total_bill < 1000:
        bill_range = "Low"
    elif total_bill <= 3000:
        bill_range = "Medium"
    else:
        bill_range = "High"

    print(f"The total bill of {i} person is {total_bill} which is {bill_range}")
