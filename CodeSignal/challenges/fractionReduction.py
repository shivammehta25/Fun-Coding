# https://app.codesignal.com/challenge/nzDQW93qQgYNGJK46
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def fractionReducing(fraction):
    g = gcd(fraction[0], fraction[1])
    return [i // g for i in fraction]
