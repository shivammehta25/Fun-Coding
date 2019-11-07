#!/usr/bin/env python
import math


def fake_swap(array):
    N = len(array)
    max_index, min_index = 0, 0
    max_value = -math.inf
    min_value = math.inf
    for i, value in enumerate(array):
        if max_value < value:
            max_value = value
            max_index = i
        if min_value >= value:
            min_value = value
            min_index = i

    if min_index > max_index:
        return (max_index + N - min_index - 1)
    else:
        return max_index + (N - min_index - 1) - 1


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    print(fake_swap(array))
