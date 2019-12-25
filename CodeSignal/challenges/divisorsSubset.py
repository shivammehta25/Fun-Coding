# https://app.codesignal.com/challenge/NYPwHxredXygQ6NPR
def divisorsSubset(subset, n):
    num_div = [0] * (n+2)
    subset = set(subset)
    for s in subset:
        for i in range(s, n+1, s):
            num_div[i] += 1
    print(num_div)
    return num_div.count(len(subset))
