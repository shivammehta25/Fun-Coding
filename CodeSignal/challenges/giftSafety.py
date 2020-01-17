# https://app.codesignal.com/challenge/ueMWmccxYbti63LXA
from itertools import permutations


def giftSafety(gift):
    total = 0
    for i in range(len(gift) - 2):
        three_letters = gift[i:i+3]
        if [''.join(x) for x in permutations(three_letters)].count(three_letters) > 1:
            total += 1

    return total
