# https://app.codesignal.com/challenge/zBDDWvf2sHC7d3Dok
def shuffledArray(shuffled):
    sum_of_array = sum(shuffled)
    op = []
    removed = False
    for s in shuffled:
        if sum_of_array - s != s or removed:
            op.append(s)
        else:
            removed = True

    return sorted(op)
