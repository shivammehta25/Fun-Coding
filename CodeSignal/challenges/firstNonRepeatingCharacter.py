# https://app.codesignal.com/challenge/jTcYipCF76HyCPDSA

def firstNotRepeatingCharacter(s):
    using = {} # { c, d } # Space Constant (26) = O(1) 
    used = {} # {a,b} # Space Constant (26) = O(1)
    # abacabad
    #        ^
    for i in s: # O(n)
        if i in using:
            used[i] = using[i]
            del using[i]
        elif i in used:
            continue
        else:
            using[i] = 1
            
    if len(using):
        for i in using:
            return i
    
    return '_'
