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
    v, a = {}, []
    for line in lines:
        if line.strip():
            if '->' in line:
                a.append(line.strip())
            else:
                x, y = line.split(':')
                v[x.strip()] = int(y)
    
    return v, a

def load_file() -> List[List[str]]:
    lines = format_lines(parse_args())
    return lines



def A(variables: Dict[str, int], algebra: List[str], print_ans=True) -> int:
    algebra = deque(algebra)

    while algebra:    
        line = algebra.popleft()

        lhs, rhs = [x.strip() for x in line.split('->')]
        a, op, b = lhs.split()
        if a in variables and b in variables:
            if op == "AND":
                variables[rhs] = variables[a] & variables[b]
            elif op == "OR":
                variables[rhs] = variables[a] | variables[b]
            elif op == "XOR":
                variables[rhs] = variables[a] ^ variables[b]
            else:
                raise ValueError(f"Invalid operation")
        else:
            algebra.append(line)
            
    z_dict = {k: str(variables[k]) for k in sorted(filter(lambda x: x.startswith('z'), variables), reverse=True)}
    ans = int("".join(z_dict.values()), 2)
    if print_ans:
        ansprint(ans)

    return ans
        
def B(variables, algebra) -> None:
    x_dict = {k: str(variables[k]) for k in sorted(filter(lambda x: x.startswith('x'), variables), reverse=True)} 
    x = int("".join(x_dict.values()), 2)
    ansprint(f"x={x}")
    y_dict = {k: str(variables[k]) for k in sorted(filter(lambda x: x.startswith('y'), variables), reverse=True)} 
    y = int("".join(y_dict.values()), 2)
    ansprint(f"y={y}")
    z_hat = x + y
    ansprint("-" * 16)
    ansprint(f"z_hat={z_hat}")
    z = A(variables, algebra, False)
    ansprint(f"z={z}")
    ansprint(f"z - z_hat = {z-z_hat}")
    

    


if __name__ == "__main__":
    variables, algebra = load_file()
    B(variables, algebra)

