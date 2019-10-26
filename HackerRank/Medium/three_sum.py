#!/usr/bin/env python3
"""
Solution to Three Sum problem, https://practice.geeksforgeeks.org/problems/triplet-sum-in-array/0
We find triplets in O(n^2) Complexity instead of regular brute force of O(n^3)

"""
def three_sum(a, s):
    """
    Gets pairs of three whose sum is 0

    Parameters:
        a : array
        s : sum to find equivalent to

    Returns:
        1 : If triplets found
        0 : if triplets not found
    """
    a.sort()
    answer_set = []
    for i in range(len(a) - 3):
        l = i+1
        r = len(a) - 1
        while r > l:
            if a[i] + a[r] + a[l] == s and a[r] > a[l] > a[i]:
                answer_set.append((a[i], a[r], a[l]))
                l += 1
            elif a[i] + a[r] + a[l] < s:
                l += 1
            else:
                r -= 1
    if answer_set:
        # print(answer_set)
        return 1
    return 0


def main():
    """
    Main Method with driver function
    """
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        n, s = map(int, input().rstrip().split())
        array = map(int, input().rstrip().split())
        print(three_sum(array, s))


if __name__ == '__main__':
    A = [-40, -20, -10, 0, 5, 10, 30, 40]
    s = 0
    assert three_sum(A, s) == 1
