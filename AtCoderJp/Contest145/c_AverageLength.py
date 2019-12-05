# https://atcoder.jp/contests/abc145/tasks/abc145_c
from itertools import permutations
import math

def distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0])**2) +  ((p1[1] - p2[1])**2))


n = int(input())
paths = []
for _ in range(n):
  x, y = map(int, input().split())
  paths.append((x, y))



paths = list(permutations(paths))
avg = 0
for path in paths:
    for i in range(len(path) - 1):
        avg += distance(path[i], path[i+1])

print(avg / len(paths))
