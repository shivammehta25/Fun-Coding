# https://app.codesignal.com/challenge/Y68W6PLmjxn7jfFei
def smallestMultiple(left, right):
    current_number = right
    checker = right
    while checker >= left:
        if current_number % checker == 0:
            checker -= 1
        else:
            current_number += 1
            checker = min(right, checker + 1)
    
    return current_number
