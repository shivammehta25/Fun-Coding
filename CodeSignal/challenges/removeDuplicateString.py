# https://app.codesignal.com/challenge/pC6LK4Ne2jHjP74Ew
def removeDuplicateStrings(inputArray):
    dump = set()
    ouput = []
    for val in inputArray:
        if val in dump:
            continue
        ouput.append(val)
        dump.add(val)
    return ouput
