# https://app.codesignal.com/challenge/aesrryCpibT2mevy6 
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)



def videoPart(part, total):
    hh1, mm1, ss1 = map(int, part.split(':'))
    hh2, mm2, ss2 = map(int, total.split(':'))
    second1 = hh1*60*60 + mm1*60 + ss1
    second2 = hh2*60*60 + mm2*60 + ss2
    g = gcd(second2, second1)
    if second1 < second2:
        return [second1/g, second2 / g]

    return [second1/g, second2 / g]




