import argparse
import heapq
import os
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cache
from pprint import pprint
from typing import List, Set

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
    
    content = [int(x.strip()) for x in args.file.readlines()]
    args.file.close()
    return content


def load_file() -> List[List[str]]:
    lines = parse_args()
    return lines



def A(nums):
    
    def mix(s ,x):
        return s ^ x
    def prune(x):
        return x % 16777216

    def secret_num(seed):
        x1 = prune(mix(seed, seed << 6))
        x2 = prune(mix(x1, x1 >> 5))
        return prune(mix(x2, x2 << 11))
    
    s = 0
    for n in nums:
        x = n
        for _ in range(2000):
            x = secret_num(x)
        print(x) 
        s += x
        
    ansprint('-' * 10)
    ansprint(s)



def B(nums):
    
    def mix(s ,x):
        return s ^ x
    def prune(x):
        return x % 16777216

    def secret_num(seed):
        x1 = prune(mix(seed, seed << 6))
        x2 = prune(mix(x1, x1 >> 5))
        return prune(mix(x2, x2 << 11))
    
    def get_sliding_window_4_and_nums(num, delta):
        sliding_window_hashes = dict()
        for i in range(5, len(delta)):
            key = tuple(delta[i-3:i+1])
            if key in sliding_window_hashes:
                continue

            sliding_window_hashes[key] = num[i]
        
        return sliding_window_hashes
    
    def merge_sliding_window_dict(all_vals, curr_window_dict):
        for tup, val in curr_window_dict.items():
            all_vals[tup] += val

        return all_vals
    
    delta = [[0] * 2000 for _ in range(len(nums))]
    num = [[0] * 2000 for _ in range(len(nums))] 
    all_vals = defaultdict(int)
    for i, n in enumerate(nums):
        x = n
        for j in range(2000):
            x = secret_num(x)
            num[i][j] = x % 10
            if j > 0:
                delta[i][j] = num[i][j] - num[i][j-1]
        curr_window_dict = get_sliding_window_4_and_nums(num[i], delta[i])

        all_vals = merge_sliding_window_dict(all_vals, curr_window_dict)
    
            
    ansprint('-' * 10)
    ansprint(list(sorted(all_vals.items(), key=lambda item: item[1], reverse=True))[:10])




if __name__ == "__main__":
    nums = load_file()
    B(nums)