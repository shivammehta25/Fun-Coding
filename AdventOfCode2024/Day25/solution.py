import argparse
import heapq
import os
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache
from pprint import pprint
from typing import Dict, List, Set, Tuple

current_dir = os.path.dirname(os.path.abspath(__file__))

log = True
ansprint = print
if log:
    print = print
    pprint = pprint
else:
    print = lambda *x: None
    pprint = print
    
def pprint2d(arr):
    for x in arr:
        row = []
        for l in x:
            row.append(l)
        print("".join(map(str, row)))
        
        
def parse_args():
    parser = argparse.ArgumentParser(description="Process a file.")
    
    parser.add_argument("-f", "--file",
                        default=f"{current_dir}/dummy_inp.txt",
                        type=argparse.FileType("r"),
                        help="Path to the input file.")
    
    args = parser.parse_args()
    
    content = [x.strip() for x in args.file.readlines()]
    args.file.close()
    return content

def format_lines(lines: List[str]) -> List[Tuple[str, str]]:
    keys, locks = [], []
    n = len(lines)
    i = 0
    while i < n:
        pattern = []
        patt_type = None
        line = lines[i].strip()
        if line[0] == '.':
            patt_type = "k"
        else:
            patt_type = 'l'
            i += 1

        for _ in range(6):
            pattern.append(lines[i])
            i += 1
        
        if patt_type == 'k':
            keys.append(pattern)
            i += 1
        else:
            locks.append(pattern)
        i += 1
        
    
    return keys, locks

def load_file() -> List[List[str]]:
    lines = format_lines(parse_args())
    return lines


def convert_to_ints(pattern: List[str]) -> List[int]:
    patt_score = [0] * len(pattern[0])
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            patt_score[j] += (1 if pattern[i][j] == '#' else 0)
    
    return patt_score

def el_sum(a, b):
    vals = all(x + y <= 5 for x, y in zip(a, b))
    return vals

def A(keys: List[List[str]], locks: List[List[str]]) -> None:
    keys = [convert_to_ints(key) for key in keys]
    locks = [convert_to_ints(lock) for lock in locks]
    
    ans = 0
    for key in keys:
        for lock in locks:
            if el_sum(key, lock):
                ans += 1

    ansprint(ans)
            
    


if __name__ == "__main__":
    keys, locks= load_file()
    A(keys, locks)