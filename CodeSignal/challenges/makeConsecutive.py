# https://app.codesignal.com/challenge/Rrq7MRnYKFhCGooeg
def makeArrayConsecutive(sequence):
    a = sorted(sequence)
    b = {i for i in range(a[0], a[len(a) - 1] + 1)}
    return sorted(b - set(a))
