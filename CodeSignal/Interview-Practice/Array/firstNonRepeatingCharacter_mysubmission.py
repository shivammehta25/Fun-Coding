# https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC

def firstNotRepeatingCharacter(s):

    d = {}
    for i, v in enumerate(s):
        if v not in d:
            d[v] = i
        else:
            d[v] = -2

    res = 10**5+1
    for i in d:
        if d[i] >= 0:
            res = min(d[i], res)

    if res > 10**5:
        return '_'

    return s[res]
