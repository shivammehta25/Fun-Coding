# https://app.codesignal.com/challenge/kzjWujHam7y7A3dzN
def findEqual(sequence):
    data = set()
    for s in sequence:
        if s in data:
            return True
        data.add(s)

    return False
