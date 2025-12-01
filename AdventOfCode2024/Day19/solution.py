import argparse
import heapq
import os
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from functools import cache
from pprint import pprint
from typing import List, Set, Tuple

from tqdm.auto import tqdm

# sys.setrecursionlimit(10000)  # Set the new recursion limit

current_dir = os.path.dirname(os.path.abspath(__file__))

log = True
ansprint = print
if log:
    print = print
    pprint = pprint
else:
    print = lambda *x: None
    pprint = print

def format_output(lines: List[str]) -> Tuple[Set[str], List[str]]:
    stripes = set([x.strip() for x in lines[0].split(',')])
    return stripes, lines[2:]
    
        
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


def load_file() -> Tuple[Set[str], List[str]]: 
    lines = parse_args()
    return format_output(lines)



def A_dfs(stripes, towels):
    # print(stripes, towels)
    
    @cache 
    def dfs(current_val, towel):
        i = 0
        while i < len(current_val) and i < len(towel):
            if current_val[i] != towel[i]:
                return False
            i += 1
        
        if i == len(current_val) == len(towel):
            return True

        found = False
        for opt in stripes:
            found = found or dfs(current_val + opt, towel)
            if found:
                break

        return found        
    
    ans = 0 
    for towel in towels:
        if dfs("", towel):
            ans += 1
    
    ansprint(ans)


def A(stripes, towels):
    
    return B(stripes, towels)

    def check_existence_itr(stripes, towel):

        possible_solutions = set([""])
        while possible_solutions:
            current_val = possible_solutions.pop()
            if len(current_val) == len(towel):
                if current_val == towel:
                    return True
                else:
                    continue
            
            for i in range(len(current_val) + 1, len(towel) + 1):
                postfix = towel[len(current_val): i]
                s = current_val + postfix
                if postfix in stripes:
                    possible_solutions.add(s)
                    
    

    def check_existence(s, i, item, towel, stack):        
        if i == len(towel):
            return

        if towel[s:s + i] in stripes:
            stack.add(towel[:s + i])

        check_existence(s, i + 1, item, towel, stack)

        return stack

 
    ans = 0 
    for towel in tqdm(towels):
        
        found = False
        l = check_existence_itr(stripes, towel)
        if l:
            found = True
        
        
        # stack = ['']
        
        # found = False
        # while stack:
        #     item = stack.pop()
        #     possible_items = set()
        #     check_existence(len(item), 1, item, towel, possible_items)
        #     # print(possible_items)
        #     stack.extend(possible_items)
        #     if len(possible_items) == 0:
        #         break
        #     elif towel in possible_items:
        #         found = True
        #         break
        
        if found: ans += 1      

    ansprint(ans)
 
 
def B(stripes, towels):

    @cache
    def count_times_can_be_made(curr_val, towel):
        if curr_val == towel:
            return 1
        if len(curr_val) == len(towel):
            return 0

        total = 0
        for i in range(len(curr_val) + 1 , len(towel) + 1):
            prefix = towel[len(curr_val) : i]
            if prefix in stripes:
                total += count_times_can_be_made(curr_val + prefix, towel)

        return total

    part_a = 0
    part_b = 0        
    for towel in tqdm(towels):
        n = count_times_can_be_made('', towel)
        part_b += n
        part_a += 1 if n > 0 else 0
                
    ansprint(part_a)
    ansprint(part_b)
 

if __name__ == "__main__":
    stripes, towels = load_file()
    B(stripes, towels)
    