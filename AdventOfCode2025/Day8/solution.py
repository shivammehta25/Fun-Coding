from collections import defaultdict
from pprint import pprint
from tqdm.auto import tqdm

from itertools import combinations

log = False
ansprint = print
if log:
    print = print
    pprint = pprint
else:
    print = lambda *x: None
    pprint = print

def load_file(path="dummy_inp.txt"):
    with open(path) as f:
        arr = f.readlines()
    
    arr = [[x for x in row.strip()] for row in arr]
    
    return arr

def distance(p1, p2):
    return abs(p2[0] - p1[0]), abs(p2[1] - p1[1])

def A(arr):
    m = len(arr)
    n = len(arr[0])
    
    antinodes = [["."] * n for _ in range(m)]
    pprint(antinodes)
    
    diff_freqs = defaultdict(list)
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] != ".":
                diff_freqs[arr[i][j]].append((i, j))
                
    pprint(diff_freqs)
    
    
    for freq, occurance in diff_freqs.items():
        combs = [x for x in range(len(occurance))]
        combs = [(occurance[a], occurance[b]) for a, b in combinations(combs, 2)]

        for comb in combs:
            mark(*comb, antinodes)
            
        
            pprint(antinodes)
            print()
    count = 0
    for i in range(m):
        for j in range(n):
            if antinodes[i][j] == "#": count += 1
    
    ansprint(count)
            
def mark(p1, p2, antinodes):
    m = len(arr)
    n = len(arr[0])

    p1, p2 = sorted([p1, p2])
    x1, y1 = p1
    x2, y2 = p2
    
    x_dist, y_dist = distance(p1, p2)
    print(p1, p2)
    print(x_dist, y_dist)
    x1_sign, y1_sign = 1, 1
    x2_sign, y2_sign = 1, 1
    if y1 <= y2:
        x1_sign = -1
        y1_sign = -1

        x2_sign = 1
        y2_sign = 1
    else:
        x1_sign = -1
        y1_sign = 1
        
        x2_sign = 1
        y2_sign = -1
        
    antinode_1 = (x1 + x1_sign * x_dist, y1 + y1_sign * y_dist)
    antinode_2 = (x2 + x2_sign * x_dist, y2 + y2_sign * y_dist)
    
    if 0 <= antinode_1[0] < m and 0 <= antinode_1[1] < n:
        antinodes[antinode_1[0]][antinode_1[1]] = "#"
    if 0 <= antinode_2[0] < m and 0 <= antinode_2[1] < n:
        antinodes[antinode_2[0]][antinode_2[1]] = "#"
        

def B(arr):
    m = len(arr)
    n = len(arr[0])
    
    antinodes = [["."] * n for _ in range(m)]
    pprint(antinodes)
    
    diff_freqs = defaultdict(list)
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] != ".":
                diff_freqs[arr[i][j]].append((i, j))
                
    pprint(diff_freqs)
    
    
    for freq, occurance in diff_freqs.items():
        combs = [x for x in range(len(occurance))]
        combs = [(occurance[a], occurance[b]) for a, b in combinations(combs, 2)]

        for comb in combs:
            markB(*comb, antinodes)
            
        
            pprint(antinodes)
            print()
    count = 0
    for i in range(m):
        for j in range(n):
            if antinodes[i][j] == "#": count += 1
    
    ansprint(count)
            
def markB(p1, p2, antinodes):
    m = len(arr)
    n = len(arr[0])

    p1, p2 = sorted([p1, p2])
    x1, y1 = p1
    x2, y2 = p2
    
    x_dist, y_dist = distance(p1, p2)
    print(p1, p2)
    print(x_dist, y_dist)
    x1_sign, y1_sign = 1, 1
    x2_sign, y2_sign = 1, 1
    if y1 <= y2:
        x1_sign = -1
        y1_sign = -1

        x2_sign = 1
        y2_sign = 1
    else:
        x1_sign = -1
        y1_sign = 1
        
        x2_sign = 1
        y2_sign = -1


    # Resonance of antinode 1   
    # x1 = x1 + x1_sign * x_dist
    while 0<= x1 < m and 0 <= y1 < n:
        antinodes[x1][y1] = "#"
        x1 = x1 + x1_sign * x_dist
        y1 = y1 + y1_sign * y_dist
    
    # Resonance of antinode 2
    # x2 = x2 + x2_sign * x_dist
    # y2 = y2 + y2_sign * y_dist
    while 0<= x2 < m and 0 <= y2 < n:
        antinodes[x2][y2] = "#"
        x2 = x2 + x2_sign * x_dist
        y2 = y2 + y2_sign * y_dist


if __name__ == "__main__":
    arr = load_file("inp.txt")
    B(arr)
