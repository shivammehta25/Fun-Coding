import argparse
import heapq
import os
import re
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from functools import cache
from pprint import pprint
from typing import List, Set, Tuple

from tqdm.auto import tqdm

digit_pattern = re.compile(r'\d+') 

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
    return lines


@dataclass
class Pos:
    x: int
    y: int
    prev: "Pos" = None

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other: "Pos") -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Pos") -> "Pos":
        return Pos(self.x + other.x, self.y + other.y, prev=self)
    
    def is_same_dir(self) -> bool:
        if self.prev is None or self.prev.prev is None:
            return True
        return self.x == self.prev.prev.x or self.y == self.prev.prev.y
    
    def __lt__(self, other) -> bool:
        return self.x < other.x if self.x != self.y else self.y < other.y

    def to_tuple(self) -> tuple[int, int]:
        return tuple((self.x, self.y))
    
    def in_bounds(self, m, n):
        return 0<= self.x < m and 0 <= self.y < n
    

def get_symbol(from_pos: Pos, to_pos: Pos) -> str:
    if to_pos.x - from_pos.x == 1 and from_pos.y - to_pos.y == 0:
        return "v"
    elif to_pos.x - from_pos.x == -1 and from_pos.y - to_pos.y == 0:
        return "^"
    elif to_pos.x - from_pos.x == 0 and to_pos.y - from_pos.y == 1:
        return ">"
    elif to_pos.x - from_pos.x == 0 and to_pos.y - from_pos.y == -1:
        return "<"
    else:
        raise ValueError(f"Need neighbours for symbol given: {from_pos} -> {to_pos}")
    
    
    
def get_path_from_node(node: Pos, path: List[Pos]):
    if node is None:
        return path
    
    path.append(node)
    return get_path_from_node(node.prev, path)


class Keyboard:
    
    def loc(self, x, y):
        if 0 <= x < self.m and 0 <= y < self.n:
            return self.keyboard[x][y]
        else:
            return "_"
        
    def dijkstra(self, s, e):
        
        directions = [Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)]
        
        nodes = [(0, s)]
        visited = set()
        while nodes:    
            cost, curr_node = heapq.heappop(nodes)
            
            if curr_node == e:
                break
            
            if curr_node in visited:
                continue
            
            visited.add(curr_node)
            
            for dir in directions:
                new_loc = curr_node + dir
                new_cost = cost + 1
                if self.loc(new_loc.x, new_loc.y) != '_' and new_loc not in visited:
                    heapq.heappush(nodes, (new_cost, new_loc))
                    
        
        return cost, curr_node
    
    def do(self, move: str) -> List[str]:
        if self.keyboard[self.arm[0]][self.arm[1]] == move:
            return ""
        ok = False
        to_move = None
        for i in range(self.m):
            for j in range(self.n):
                # print(i, j, self.loc(i, j), move)
                if self.loc(i, j) == move:
                    to_move = Pos(i, j)
                    ok = True
                    break
            if ok:
                break
        
        cost, curr_node = self.dijkstra(Pos(self.arm[0], self.arm[1]), to_move)
        path = []
        path = get_path_from_node(curr_node, path)
        symbols = []
        for move in path:
            if move.prev is not None:
                symbols.append(get_symbol(move.prev, move))
        self.arm = curr_node.to_tuple()  
        return "".join(symbols)
    
class NumericKeyboard(Keyboard):
    def __init__(self, arm: Pos = Pos(3, 2)):
        self.arm: tuple[int, int] = arm.to_tuple()
        self.keyboard = [
            "789",
            "456",
            "123",
            "_0A"
        ]
        self.m = 4
        self.n = 3

class DirectionalKeyboard(Keyboard):
    def __init__(self, arm: Pos = Pos(0, 2)):
        self.arm: tuple[int, int] = arm.to_tuple()
        self.keyboard = [
            "_^A",
            "<v>",
        ]
        self.m = 2
        self.n = 3
   

        
def A(lines):
    k = NumericKeyboard()
    d1 = DirectionalKeyboard()
    d2 = DirectionalKeyboard()
    
    ans = []
    for line in lines:
        num_moves = []
        for c in line:
            num_moves.append(k.do(c))
            num_moves.append('A')
        num_moves = "".join(num_moves)
        print(num_moves)
        d1_moves = []
        for move in num_moves:
            d1_moves.append(d1.do(move))
            d1_moves.append('A')
        d1_moves = "".join(d1_moves)
        print(d1_moves)
        d2_moves = []
        for move in d1_moves:
            d2_moves.append(d2.do(move))
            d2_moves.append('A')
        d2_moves = "".join(d2_moves)
        print(d2_moves)
        l = len(d2_moves)
        num = int(digit_pattern.findall(line)[0])
        ans.append(l * num)
        ansprint(ans[-1])
    
        break





if __name__ == "__main__":
    grid = load_file()
    A(grid)