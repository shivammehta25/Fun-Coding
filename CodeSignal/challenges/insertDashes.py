# https://app.codesignal.com/challenge/PLyDoCvsWjCNpSFux
def insertDashes(inputString):
    s = []
    for c in inputString:
        if c == ' ':
            s.pop()
            s.append(c)
        else:
            s.append(c)
            s.append('-')
    s.pop()

    return ''.join(s)
