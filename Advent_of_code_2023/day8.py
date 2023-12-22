import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import cycle
from pprint import pprint

from helpers import read_file
from tqdm.auto import tqdm

# data = read_file("inputs/day8_test_a.txt")
# data = read_file("inputs/day8_test_b.txt")
# data = read_file("inputs/day8_test_c.txt")
data = read_file("inputs/day8.txt")

class Node:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right 
    def __repr__(self) -> str:
        return f"Node({self.left}, {self.right})"

def formatter():
    instructions = data[0].strip()
    values = {}
    for line in data[2:]:
        source,  left_right = line.split("=")
        left, right = re.search(r'\((.*?)\)',left_right).group(1).split(',')
        values[source.strip()] = Node(left.strip(), right.strip())
    
    return instructions, values


def A():
    instructions, values = formatter()
    # pprint(instructions)
    # pprint(values)
    looped_instructions = cycle(instructions)
    current_node = "AAA"
    steps_taken = 0
    while current_node != "ZZZ":
        # print("\rSteps_taken: ", steps_taken, end="")
        steps_taken += 1
        instruction = next(looped_instructions)
        if instruction == "L":
            current_node = values[current_node].left
        elif instruction == "R":
            current_node = values[current_node].right
        else:
            raise ValueError(f"Invalid instruction: {instruction}")
        
    print(steps_taken)
    
    
def B():
    instructions, values = formatter()
    # pprint(instructions)
    # pprint(values)
    looped_instructions = cycle(instructions)
    current_nodes = [x for x in values if x[-1] == "A"]
    steps_taken = 0
    saved_values = []
    
    for instruction in looped_instructions:
        steps_taken += 1
        print("\rSteps_taken: ", steps_taken, end=" ")

        for i, _ in enumerate(current_nodes):
            if instruction == "L":
                current_nodes[i] = values[current_nodes[i]].left
            else:
                current_nodes[i] = values[current_nodes[i]].right
            
        new_nodes = []
        for node in current_nodes:
            if node[-1] == "Z":
                saved_values.append(steps_taken)
                continue
        
            new_nodes.append(node)
        print(new_nodes) 
        if not new_nodes:
            break

        current_nodes = new_nodes

    print(math.lcm(*saved_values))
    
if __name__ == "__main__":
    # A()
    B()
    
    
    
        
        
        
        
    