#!/usr/bin/env python3
# https://codeforces.com/problemset/problem/1256/A


def coin_possibility(a, b, n, S):
    """
    a is the number of n coins
    b is the number of 1 coins
    S is the total sum required to pay
    """

    total_sum_available = a*n + b
    if total_sum_available < S:
        return 'NO'

    if b < (S % n):
        return 'NO'

    return 'YES'


if __name__ == '__main__':
    n_test = int(input())
    answer = []
    for _ in range(n_test):
        a, b, n, S = list(map(int, input().split()))
        answer.append(coin_possibility(a, b, n, S))
    [print(i) for i in answer]
