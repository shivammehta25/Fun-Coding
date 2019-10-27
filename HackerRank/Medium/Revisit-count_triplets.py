#!/bin/usr/env python3
"""
URL: https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
I feel it is populating like in dynamic but you don't populate all just those
that tend to be triplets
So, the trick is to have multiple dictionaries, each containing values for
their potential to be one of them i.e if the dictionary is potential_two that
means that this value has this number of times chance to be in a triplet if i
found third element, same with potential three will give me the final count
if i found potential three i will increment my count
"""

import os
from collections import defaultdict


def count_triplets(arr, r):
    potential_two = defaultdict(int)
    potential_three = defaultdict(int)
    count = 0
    for i in arr:
        count += potential_three[i]
        potential_three[i*r] += potential_two[i]
        potential_two[i*r] += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = count_triplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
