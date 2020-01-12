# https://app.codesignal.com/challenge/mXCWzh37ibxEY822h
def countSumOfTwoRepresentations3(n, l, r):
    number_of_ways = 0
    i = 1
    while i <= n - i:
        if l <= i and n - i <= r:
            number_of_ways += 1
        i += 1

    return number_of_ways
