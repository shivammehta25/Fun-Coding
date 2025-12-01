import argparse
import heapq
import os
from collections import defaultdict
from dataclasses import dataclass
from pprint import pprint
from typing import Dict, List, Tuple

from tqdm.auto import tqdm

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
    
    register = {'A': 0, 'B': 0, 'C': 0}
    get_register = lambda idx: int(content[idx].split(':')[1].strip())
    register['A'] = get_register(0)
    register['B'] = get_register(1)
    register['C'] = get_register(2)

    operations = []
    for i, _ in enumerate((vals := list(map(int, content[4].split(':')[1].split(','))))):
        if i % 2 == 0:
            operations.extend([vals[i], vals[i + 1]])
    
    args.file.close()
    return register, operations 


def load_file() -> Tuple[Dict[str, int], List[int]]:
    lines = parse_args()
    return lines

@dataclass
class Operation:
    opcode: int
    operand: int





def action(registers: Dict[str, int], operation: Operation, output: List[int]):
    combo_operators = {0: 0, 1: 1, 2: 2, 3: 3, 4: registers['A'], 5: registers['B'], 6: registers['C']}
    literal_operators = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5:5, 6:6, 7:7}
    if operation.opcode == 0:
        if registers['A'] > 0:
            registers['A'] = registers['A'] // (2**combo_operators[operation.operand])
    elif operation.opcode == 1:
        registers['B'] ^= literal_operators[operation.operand]
    elif operation.opcode == 2:
        registers['B'] = combo_operators[operation.operand] % 8
    elif operation.opcode == 3:
        if registers['A'] != 0:
            return literal_operators[operation.operand]
    elif operation.opcode == 4:
        registers['B'] ^= registers['C']
    elif operation.opcode == 5:
        output.append(combo_operators[operation.operand] % 8)
    elif operation.opcode == 6:
        if registers['A'] > 0:
            registers['B'] = registers['A'] // (2**combo_operators[operation.operand]) 
    elif operation.opcode == 7:
        if registers['A'] > 0:
            registers['C'] = registers['A'] // (2**combo_operators[operation.operand])
    else:
        raise ValueError("huh?")
    
def B(registers: Dict[str, int], operations: List[int]) -> None:
    for i in tqdm(range(10000000, 100000000)):
        output = run_A_compiled(i)
        # tqdm.write(str(output))
        if output == operations:
            break
    
    ansprint(i)
        
            



def A(registers: Dict[str, int], operations: List[int], print_ans=True) -> List[int]:
    
    output = []
    
    inst = 0
    
    while inst < len(operations) - 1:
        op = Operation(operations[inst], operations[inst + 1])
        step_out = action(registers,  op, output)
        if step_out is not None:
            inst = step_out
            continue
    
        inst += 2
    if print_ans:
        ansprint(",".join(map(str, output)))
        
    return output

def A2(registers, operations):
    ansprint(run_A_compiled(registers['A']))

def run_A_compiled(a):
    b = c = 0
    out = []
    while a:
        b = a % 8
        b ^= 1
        c = a // (1 << b)
        b ^= 5
        b ^= c
        out.append(b % 8)
        a //= 8

    return out
        
        
    

if __name__ == "__main__":
    registers, operations = load_file()
    A(registers, operations)
    
    