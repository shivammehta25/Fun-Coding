#/usr/bin/env python3
"""
Solution to problem: https://practice.geeksforgeeks.org/problems/adding-ones/0
We reduced the runtime of algorithm from O(nm) to O(n+m) resulting in
half the time running
"""


def get_array(array, n):
    """
    gets the array

    Gets input and returns final computed value

    Parameters:
        array: list
        n : integer

    returns:
        n : list of added ones
    """
    n = [0 for _ in range(n)]
    d_count = dict()
    array = [i - 1 for i in array]
    for i in array:
        if i not in d_count:
            d_count[i] = 0
        d_count[i] += 1
    k = 0
    for i in range(len(n)):
        if i not in d_count:
            d_count[i] = 0
        n[i] = d_count[i] + k
        k = n[i]

    return n


def main():
    """
    This is the driver method
    """
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        array = list(map(int, input().rstrip().split()))
        print(' '.join(map(str, get_array(array, n))))


if __name__ == '__main__':
    main()
