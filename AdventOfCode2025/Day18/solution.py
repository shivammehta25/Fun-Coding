import argparse
import heapq
import os
from collections import defaultdict
from dataclasses import dataclass
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
    
    content = [x.strip() for x in args.file.readlines()]
    args.file.close()
    return [(int(b), int(a)) for a,b in [x.split(',') for x in content]]


def load_file() -> List[List[str]]:
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


def A(bytes):
    # m, n, s = 7, 7, 12
    m, n, s = 71, 71, 1024

    
    grid = bytes2grid(bytes, m, n, s)
        
    _, w = dijkstra_algorithm(m, n, grid, print_path=True)
    ansprint(w)
    
    

def bytes2grid(bytes, m, n, s):
    grid = [['.'] * n for _ in range(m)]
    for i, (x, y) in enumerate(bytes[:s]):
        grid[x][y] = '#'
    return grid


def dijkstra_algorithm(m, n, grid, print_path=False):
    start = Pos(0, 0)
    end = Pos(m-1, n-1)

    priority_queue = [(0, start)]
    weights = defaultdict(lambda: float("inf")) 
    visited = set()
    
    directions = [Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)]
    found = False
    
    while priority_queue:
        curr_weight, current_pos = heapq.heappop(priority_queue)
        
        if current_pos in visited:
            continue
        
        if current_pos == end:
            found = True
            break
        
        visited.add(current_pos)
        for dir in directions:
            new_p = current_pos + dir
            
            if new_p in visited or not new_p.in_bounds(m, n) or grid[new_p.x][new_p.y] == '#':
                continue
            
            curr_step_cost = 1 + curr_weight
            if curr_step_cost < weights[new_p]:
                weights[new_p] = curr_step_cost
                heapq.heappush(priority_queue, (curr_step_cost, new_p))
                
    if print_path:
        path = []
        while current_pos.prev is not None:
            path.append(current_pos.to_tuple())
            current_pos = current_pos.prev
        
        for (x, y) in path:
            grid[x][y] = 'X' # weights[Pos(x, y)]
            
        pprint2d(grid)
    
    return found, curr_weight

def B(bytes):
    # m, n = 7, 7
    m, n = 71, 71
    print(len(bytes))
    for s in range(286, len(bytes)):
        grid = bytes2grid(bytes, m, n, s)
        
        found, w = dijkstra_algorithm(m, n, grid, print_path=False)
        print(s, w)
        if not found:
            break
        
    ansprint()
    ansprint(",".join(map(str, list(reversed(bytes[s - 1])))))

if __name__ == "__main__":
    bytes = load_file()
    B(bytes)