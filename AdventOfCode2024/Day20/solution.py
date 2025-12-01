import argparse
import os
from collections import Counter, defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from pprint import pprint
from typing import List, Set

current_dir = os.path.dirname(os.path.abspath(__file__))

log = False
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
    
    content = [[a for a in x.strip()] for x in args.file.readlines()]
    args.file.close()
    return content


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



def get_path(node, path=[]):

    if node is None:
        return list(reversed(path))
    
    path.append(node)
    return get_path(node.prev)
        
        

def bfs(grid, s, e):
    m = len(grid)
    n = len(grid)
    directions = [Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)]
    path = dict()
    nodes = deque([(s, 0)])
    visited = [[False] * m for _ in range(n)]
    found_cost = 0
    while nodes:
        node, curr_cost = nodes.popleft()
        path[node] = curr_cost
        if node == e:
            found_cost = curr_cost
            break
        
        for dir in directions:
            next_dir = node + dir
            val = grid[next_dir.x][next_dir.y]
            if next_dir.in_bounds(m, n) and not visited[next_dir.x][next_dir.y] and (val == '.' or val.isdigit() or val == 'E'):
                nodes.append((next_dir, curr_cost+1))
                visited[next_dir.x][next_dir.y] = True
     
    return path, found_cost


def find_cheats(path, d=2):
    vals = []
    for p in path:
        for dx in range(-d, d+1):
            for dy in range(-d, d+1):
                if dx == dy == 0 or (abs(dx) + abs(dy) > d):
                    continue
                next_p = p + Pos(dx, dy)
                if next_p in path:
                    vals.append(path[next_p] - path[p] - (abs(dx) + abs(dy)))
    
    return sorted(vals, reverse=True)


def answer(grid, min=1, cheat_len=2):
    pprint2d(grid)
    m = len(grid)
    n = len(grid[0])
    s, e = None, None 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                s = Pos(i, j)
            elif grid[i][j] == 'E':
                e = Pos(i, j)

    
    path, cost = bfs(grid, s, e)
    print(cost)
    cheats = find_cheats(path, cheat_len)
    print(sorted(dict(Counter(cheats)).items(), reverse=True))
    ansprint(sum(1 for k in cheats if k >= min))
    

if __name__ == "__main__":
    grid = load_file()
    part_a = {'min': 100, 'cheat_len': 2}
    # answer(grid, **part_a)
    part_b = {'min': 100, 'cheat_len': 20}
    answer(grid, **part_b)

    
    # d = 2
    # arr = [['.'] * 5 for _ in range(5)]
    # s = (2, 2)
    # pprint2d(arr)
    # for dx in range(-d, d+1):
    #     for dy in range(-d, d+1):
    #         if dx == dy == 0 or (abs(dx) + abs(dy) > 2):
    #             continue
                
    #         arr[2 + dx][2 + dy] = 'X'
            
    # pprint2d(arr)