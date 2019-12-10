# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys
from collections import deque

# Complete the climbingLeaderboard function below.


def maintain_leaderboard(score):
    # Complexity Time: O(N),  Space: O(N)
    unique_score = []
    for i in range(len(score)):
        if not unique_score:
            unique_score.append(score[i])
            continue
        if score[i] != unique_score[-1]:
            unique_score.append(score[i])
    return unique_score


def climbingLeaderboard(score, alice):
    """
    This is a two pointer approach to problem which will result in better
    complexity than the regular binary which is O(NlogM), while this is 
    just O(N + M), space comlexity = O(N)
    """
    final_ranks = []
    score = maintain_leaderboard(score)  # O(N)
    score_ptr = len(score) - 1
    alice_ptr = 0
    while alice_ptr < len(alice) and score_ptr >= 0:  # O(N + M)
        if alice[alice_ptr] < score[score_ptr]:
            final_ranks.append(score_ptr + 2)
        elif alice[alice_ptr] == score[score_ptr]:
            final_ranks.append(score_ptr + 1)
        else:
            score_ptr -= 1
            continue
        alice_ptr += 1
    # if any element left which are greater than the maximum score
    while alice_ptr < len(alice):
        final_ranks.append(1)
        alice_ptr += 1

    return final_ranks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
