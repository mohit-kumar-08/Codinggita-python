"""to define a function, calculate_result()"""

def calculate_result(marks, passing_marks = 35):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"
