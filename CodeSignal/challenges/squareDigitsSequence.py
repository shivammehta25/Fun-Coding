# https://app.codesignal.com/challenge/YPAhD7Tz3o3E4vwBi
def squareDigitsSequence(a0):
    values = set()
    values.add(a0)
    while True:
        sum_sq = 0  # 0
        for i in str(a0):
            sum_sq += int(i)**2
        if sum_sq in values:
            break
        values.add(sum_sq)
        a0 = sum_sq

    return(len(values) + 1)
