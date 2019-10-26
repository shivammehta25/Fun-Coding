#!/bin/python3
"""
URL: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Generate anagrams and with the help of itertool combinations find all pairs that are equal
"""


import math
import os
import random
import re
import sys
from itertools import combinations
from collections import defaultdict
# Complete the sherlockAndAnagrams function below.



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



def sherlockAndAnagrams(s):
    pair= 0
    anagrams = generate_anagram(s)
    for length in anagrams:
        for (a,b) in combinations(anagrams[length], 2):
            if sorted(a) == sorted(b):
                pair += 1
    return pair



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
