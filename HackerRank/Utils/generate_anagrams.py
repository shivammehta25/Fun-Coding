#!/usr/bin/env python3
"""
This Utility generates and return anagrams by sliding windows can be used in
any program
"""
from collections import defaultdict


def generate_anagram(a):
    """
    Input list and returns dictionary with keys length = len(a) and for each
    value will be anagram of its size
    """
    grams = defaultdict(list)
    N = len(a)
    for i in range(N):
        windows_length = i + 1
        for j in range(N-windows_length+1):
            grams[i].append(a[j:j+windows_length])
    return grams


if __name__ == '__main__':
    print(generate_anagram(input()))
