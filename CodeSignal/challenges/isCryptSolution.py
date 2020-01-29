# https://app.codesignal.com/challenge/KkRXXEt9DwaHFYk2K
def isCryptSolution(crypt, solution):
    w = []
    solution = { a[0]:a[1] for a in solution }
    for v in crypt:
        w.append([solution[c] for c in v])
    
    for v in w:
        if len(v) > 1 and v[0] == '0':
            return False
        
    return int(''.join(w[0])) + int(''.join(w[1])) == int(''.join(w[2]))
