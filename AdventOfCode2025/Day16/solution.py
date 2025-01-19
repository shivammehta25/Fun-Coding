import argparse
import heapq
import os
from collections import defaultdict, deque
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
    
def pprint2d(arr, tabs=True):
    for x in arr:
        row = []
        for l in x:
            row.append(l)
        if not tabs:
            print("".join(map(str, row)))
        else:
            print("\t".join(map(str, row)))
        
        
def parse_args():
    parser = argparse.ArgumentParser(description="Process a file.")
    
    parser.add_argument("-f", "--file",
                        default=f"{current_dir}/dummy_inp.txt",
                        type=argparse.FileType("r"),
                        help="Path to the input file.")
    
    args = parser.parse_args()
    
    content = [[l for l in x.strip()] for x in args.file.readlines()]
    args.file.close()
    return content


def load_file() -> List[List[str]]:
    lines = parse_args()
    return lines

class Pos:
    def __init__(self, x, y, prev=None):
        self.x: int = x
        self.y: int = y
        self.prev: "Pos" = prev
        self.path = set()
        self.came_from = set([prev])

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other: "Pos") -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Pos") -> "Pos":
        new_pos = Pos(self.x + other.x, self.y + other.y, prev=self)
        new_pos.path = self.path.copy()
        new_pos.path.add(self)
        return new_pos
    
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


def A(grid: List[List[str]]):
    m = len(grid)
    n = len(grid[0])
    
    directions = [Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)]
    start_pos, end_pos = (-1, -1), (-1, -1)
    weights = {}
    for x in range(m):
        for y in range(n):
            if grid[x][y] == 'S':
                start_pos = Pos(x, y, Pos(x, 0))
                weights[start_pos] = 0
            elif grid[x][y] == "E":
                end_pos = Pos(x, y)
                weights[end_pos] = float("inf")
            else:
                weights[Pos(x, y)] = float('inf')
    print(start_pos, end_pos)
    
    priority_queue = [(0, start_pos)]
    visited = set()
    
    while priority_queue:
        curr_weight, current_pos = heapq.heappop(priority_queue)
        
        if current_pos == end_pos:
            break

        if current_pos in visited:
            continue
        
        
        visited.add(current_pos)
        
        for neighbour in directions:
            new_p = current_pos + neighbour
            
            if new_p in visited:
                continue

            if grid[new_p.x][new_p.y] == "#":
                continue
            
            cost = 1 if new_p.is_same_dir() else 1001
            move_cost = curr_weight + cost
            if curr_weight < weights[new_p]:
                weights[new_p] = move_cost
                heapq.heappush(priority_queue, (move_cost, new_p))
 
    
    path = []
    while current_pos.prev is not None:
        path.append(current_pos.to_tuple())
        current_pos = current_pos.prev
    
    for (x, y) in path:
        grid[x][y] = weights[Pos(x, y)]
        
    pprint2d(grid)
    
    print(curr_weight)
    

    
    
if __name__ == "__main__":
    grid = load_file()
    A(grid)