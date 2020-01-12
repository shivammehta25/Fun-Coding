# https://app.codesignal.com/challenge/a8GNsYr8FQxZmMhJj
from math import factorial


def countWays(n, k):
    if n < k:
        return 0
    return (factorial(n) // (factorial(k) * factorial(n-k))) % (10**9 + 7)
