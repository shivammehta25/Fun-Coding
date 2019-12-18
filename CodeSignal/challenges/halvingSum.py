# https://app.codesignal.com/challenge/mJPidEuuPJ8vCh6sh
def get_sum(s, n):
    if n == 0:
        return 0
    s += get_sum(s, n // 2)
    print(s, n)

    return n + s


def halvingSum(n):
    s = 0
    return get_sum(s, n)
