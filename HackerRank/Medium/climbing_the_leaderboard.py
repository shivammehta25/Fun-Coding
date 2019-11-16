#!/bin/python3
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/
import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.

def generate_rank(score):
    score_updated = []
    p = math.inf
    rank = 1
    for c in score:
        if p != c:
            score_updated.append((c, rank))
            rank += 1
            p = c
    return score_updated

def check_rank(score, n):
    if n > score[0][0]:
        return 1
    elif n < score[-1][0]:
        return score[-1][1] + 1
    else:
        l = 0
        r = len(score) - 1
        while(l <= r):
            print(l, r)
            m = r - ((r - l) // 2)
            if score[m][0] == n:
                return score[m][1]
            elif score[m][0] < n :
                r = m - 1
            else:
                l = m + 1
        return score[r][1] + 1

def climbingLeaderboard(score, alice):
    r = []
    score = generate_rank(score)
    for n in alice:
        r.append(check_rank(score, n))
    
    return r

if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    inpttr = open('input.txt', 'r')
    scores_count = int(inpttr.readline())

    scores = list(map(int, inpttr.readline().rstrip().split()))

    alice_count = int(inpttr.readline())

    alice = list(map(int, inpttr.readline().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    inpttr.close()
    fptr.close()
