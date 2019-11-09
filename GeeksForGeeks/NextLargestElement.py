#!/usr/bin/env python3
# https://www.geeksforgeeks.org/next-greater-element/#:~:targetText=For%20any%20array%2C%20rightmost%20element,each%20element%20are%20as%20follows.


def next_largest_integer(a):
    s = [0]
    N = len(a)
    o = [0] * N
    for i in range(1, N):
        if s:
            current_value = a[i]
            top = s[-1]

            while current_value > a[top]:
                o[s.pop()] = current_value
                if not s:
                    break
                top = s[-1]
        s.append(i)

    while s:
        o[s.pop()] = -1

    return o


if __name__ == '__main__':
    n = int(input())
    output = []
    for _ in range(n):
        input()
        output.append(next_largest_integer(list(map(int, input().split()))))

    [print(' '.join(map(str, o))) for o in output]
