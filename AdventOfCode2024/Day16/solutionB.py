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
        """
        Returns True if we're continuing in the same axis
        as we moved in the previous step. Otherwise, it's a turn.
        """
        if self.prev is None or self.prev.prev is None:
            # If no previous history, treat as "same direction"
            return True
        # Compare (x,y) to (prev.prev.x, prev.prev.y):
        return (self.x == self.prev.prev.x) or (self.y == self.prev.prev.y)

    def __lt__(self, other) -> bool:
        """Tie-breaker for heapq (not used much here, but required)."""
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

    def to_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)

    def in_bounds(self, m, n):
        return 0 <= self.x < m and 0 <= self.y < n

def B(grid: List[List[str]]):

    def dijkstra(grid, s: Pos, e: Pos, weights):
        """
        Modified Dijkstra that returns ALL minimum-cost paths.
        Costs:
          - 1 if going straight (same direction)
          - 1001 if turning
        """
        m = len(grid)
        n = len(grid[0])
        directions = [Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)]

        # Priority queue holds: (cost_so_far, current_node, path_so_far)
        pq = []
        
        # We'll keep track of paths in a dict: paths[node] = [list_of_paths]
        paths = defaultdict(list)
        
        # Initialize for the start node
        heapq.heappush(pq, (0, s, [s]))
        paths[s] = [[s]]  # one path: [s]

        while pq:
            curr_w, node, path_so_far = heapq.heappop(pq)
            
            # If we've already found a cheaper route to node, skip
            if curr_w > weights[node]:
                continue

            # Explore neighbors
            for dir in directions:
                next_dir = node + dir
                if not next_dir.in_bounds(m, n):
                    continue

                # Check wall
                if grid[next_dir.x][next_dir.y] == '#':
                    continue

                # Determine cost for this move
                move_cost = 1 if next_dir.is_same_dir() else 1001
                new_cost = curr_w + move_cost

                # If we found a strictly cheaper cost
                if new_cost < weights[next_dir]:
                    weights[next_dir] = new_cost
                    # Overwrite the paths with this new better path
                    new_path = path_so_far + [next_dir]
                    paths[next_dir] = [new_path]
                    heapq.heappush(pq, (new_cost, next_dir, new_path))
                
                # If this cost ties the best known cost for next_dir
                elif new_cost == weights[next_dir]:
                    # Append this path as an additional equally optimal path
                    new_path = path_so_far + [next_dir]
                    paths[next_dir].append(new_path)
                    # We also need to push so we can continue expanding from next_dir
                    # at this same cost if needed.
                    heapq.heappush(pq, (new_cost, next_dir, new_path))

        # Return all minimal paths for e (or empty if none), and the min cost
        return paths[e], weights[e]

    m = len(grid)
    n = len(grid[0])

    # Identify S, E
    start_pos, end_pos = None, None
    weights = {}

    for x in range(m):
        for y in range(n):
            cell = grid[x][y]
            pos_obj = Pos(x, y)
            if cell == 'S':
                # We'll seed "prev" to avoid None checks
                start_pos = Pos(x, y, prev=Pos(x, y))
                weights[start_pos] = 0
            elif cell == 'E':
                end_pos = Pos(x, y)
                weights[end_pos] = float('inf')
            else:
                weights[pos_obj] = float('inf')

    print(start_pos, end_pos)  # debug

    # Run modified Dijkstra
    all_paths, min_cost = dijkstra(grid, start_pos, end_pos, weights)

    if not all_paths:
        print("No path found from S to E.")
        return

    print(f"Found {len(all_paths)} path(s) with cost = {min_cost}.\n")

    # Mark the first path for demonstration
    # (You could mark them all in the grid, but it might get messy.)
    path_to_mark = all_paths[0]
    for p in path_to_mark:
        if grid[p.x][p.y] not in ('S', 'E', '#'):
            grid[p.x][p.y] = 'X'

    pprint2d(grid)
    print("\nALL MIN-COST PATHS:")
    for idx, pth in enumerate(all_paths, start=1):
        print(f"Path #{idx}: {pth}")


if __name__ == "__main__":
    grid = load_file()
    B(grid)
