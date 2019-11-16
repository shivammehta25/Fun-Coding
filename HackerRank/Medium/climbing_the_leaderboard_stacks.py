#!/bin/python3
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/

import math
import os
import random
import re
import sys
from collections import deque



def climbingLeaderboard(score, alice):
    score_q = deque()
    prev = math.inf
    for element in score:
        if element != prev:
            score_q.append(element)
            prev = element

    rank = len(score_q) + 1
    r = []
    p_a = 0
    top_element = score[0]
    while p_a < len(alice):
        if score_q:
            current_leader = score_q.pop()
        
        if alice[p_a] < current_leader:
            r.append(rank)
            p_a += 1
            while p_a < len(alice) and alice[p_a] < current_leader:
                r.append(rank)
                p_a += 1
                
        elif alice[p_a] == current_leader:
            r.append(rank-1)
            p_a += 1
            while p_a < len(alice) and alice[p_a] == alice[p_a - 1]:
                r.append(rank - 1)
                p_a += 1

        elif alice[p_a] > top_element:
            r.append(1)
            p_a += 1

        rank -= 1

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

