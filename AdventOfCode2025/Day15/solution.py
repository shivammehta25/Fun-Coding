import argparse
import re
import sys
import time
from dataclasses import dataclass
from itertools import chain
from pprint import pprint
from typing import List, Set

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
        print("".join(row))
        
def parse_args():
    parser = argparse.ArgumentParser(description="Process a file.")
    
    parser.add_argument("-f", "--file",
                        default="Day15/dummy_inp2.txt",
                        type=argparse.FileType("r"),
                        help="Path to the input file.")
    
    args = parser.parse_args()
    
    content = [x.strip() for x in args.file.readlines()]
    args.file.close()
    return content


def load_file():
    lines = parse_args()
    grid, moves = [], []
    for line in lines:
        if line:
            if "#" in line:
                grid.append([x for x in line])
            else:
                moves.append([x for x in line])
    
    moves = list(chain(*moves))
    
    return grid, moves

@dataclass
class Pos:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __add__(self, other: "Pos") -> "Pos":
        return Pos(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Pos") -> "Pos":
        other.x *= -1
        other.y *= -1
        return self + other

    def __eq__(self, value: "Pos") -> bool:
        return self.x == value.x and self.y == value.y
    
    def __neg__(self):
        return Pos(-self.x, -self.y)
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    @property
    def GPS(self) -> int:
        return self.x * 100 + self.y
    

class Board:
    def __init__(self, robot: Pos, boxes: Set[Pos], walls: Set[Pos], n_rows: int, m_cols: int):
        self.robot = robot
        self.boxes = boxes
        self.walls = walls
        self.n_rows = n_rows
        self.m_columns = m_cols

    
    @classmethod
    def from_grid(cls, grid: List[List[str]]):
        m = len(grid)
        n = len(grid[0])
        robot = None
        walls, boxes = set(), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@': robot = Pos(i, j)
                elif grid[i][j] == "#": walls.add(Pos(i, j))
                elif grid[i][j] == "O": boxes.add(Pos(i, j))
        
        return cls(robot, boxes, walls, m, n)
    
    @property
    def grid(self):
        grid = [["."] * self.m_columns for _ in range(self.n_rows)]
        for wall in self.walls:
            grid[wall.x][wall.y] = '#'
        
        for box in self.boxes:
            grid[box.x][box.y] = 'O'
        
        grid[self.robot.x][self.robot.y] = '@'
        
        return grid

    def move(self, dir: Pos):
        curr_robot_pos = self.robot + dir
        print(curr_robot_pos)
        if curr_robot_pos in self.walls:
            print("Hit a wall")
            return
        
        move = True

        if curr_robot_pos in self.boxes:

            def move_box(pos, dir):
                if pos not in self.boxes and pos not in self.walls and self.robot != pos:
                    return True
                if pos in self.walls or pos == self.robot:
                    return False

                if pos in self.boxes:
                    success = move_box(pos + dir, dir)
                    if not success:
                        return False
                    else:
                        self.boxes.remove(pos)
                        self.boxes.add(pos + dir)
                                
                return True
              
            move = move_box(curr_robot_pos, dir)
            
        if move:
            self.robot = curr_robot_pos
        

    def move_up(self):
        up = Pos(-1, 0)
        self.move(up)
    
    def move_down(self):
        down = Pos(1, 0)
        self.move(down)
    
    def move_left(self):
        left = Pos(0, -1)
        self.move(left)
    
    def move_right(self):
        right = Pos(0, 1)
        self.move(right)
    
    @property
    def GPS(self):
        ans = 0
        for box in self.boxes:
            ans += box.GPS
            
        return ans
    

class WideBox:
    def __init__(self, start_pos: Pos) -> None:
        self.start_pos = start_pos
        self.end_pos = start_pos + Pos(0, 1)
        
    @property
    def loc(self):
        return (self.start_pos, self.end_pos)
    
    def __eq__(self, value: object) -> bool:
        return self.start_pos == value.start_pos and self.end_pos == value.end_pos
    
    def __repr__(self) -> str:
        return f"[{self.start_pos} - {self.end_pos}]"
    
    def __hash__(self) -> int:
        return hash((self.start_pos, self.end_pos))
    
    def move_left(self) -> None:
        self.start_pos += Pos(0, -1)
        self.end_pos += Pos(0, -1)
        
    def move_right(self) -> None:
        self.start_pos += Pos(0, 1)
        self.end_pos += Pos(0, 1)
        
    def move_up(self) -> None:
        self.start_pos += Pos(-1, 0)
        self.end_pos += Pos(-1, 0)
        
    def move_down(self) -> None:
        self.start_pos += Pos(1, 0)
        self.end_pos += Pos(1, 0)
        
    def move_with_pos(self, pos: Pos) -> None:
        self.start_pos += pos
        self.end_pos += pos
        
    def add_pos(self, pos: Pos) -> "WideBox":
        start_pos = self.start_pos + pos
        return WideBox(start_pos)
    
    def in_wall(self, walls: List[Pos]) -> bool:
        return self.start_pos in walls or self.end_pos in walls
    
    @property
    def GPS(self) -> int:
        return self.start_pos.GPS

class WideBoard(Board):
    
    @classmethod
    def from_grid(cls, grid: List[List[str]]):
        m = len(grid)
        n = len(grid[0])
        robot = None
        walls, boxes = set(), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@': robot = Pos(i, 2*j)
                elif grid[i][j] == "#": 
                    walls.add(Pos(i, 2*j))
                    walls.add(Pos(i, 2*j + 1))
                elif grid[i][j] == "O": 
                    boxes.add(WideBox(Pos(i, 2*j)))

        return cls(robot, boxes, walls, m, n * 2)
    
    @property
    def grid(self):
        grid = [["."] * self.m_columns for _ in range(self.n_rows)]
        for wall in self.walls:
            grid[wall.x][wall.y] = '#'
        
        for box in self.boxes:
            start, end = box.loc
            grid[start.x][start.y] = "["
            grid[end.x][end.y] = "]"        
        
        grid[self.robot.x][self.robot.y] = '@'
        
        return grid
    
    @property
    def GPS(self):
        ans = 0
        for box in self.boxes:
            ans += box.GPS

        return ans
    
    def move_up(self):
        up = Pos(-1, 0)
        self.move(up, vert=True)
    
    def move_down(self):
        down = Pos(1, 0)
        self.move(down, vert=True)
    
    def move_left(self):
        left = Pos(0, -1)
        self.move(left)
    
    def move_right(self):
        right = Pos(0, 1)
        self.move(right, right=True)


    def move(self, dir: Pos, boxes: Set[WideBox]= None, right=False, vert=False):
        def move_box(box_pos: WideBox, dir: Pos, all_boxes: Set[WideBox], depth=1):

            if box_pos not in all_boxes and (box_pos.add_pos(Pos(0, -1)) not in all_boxes) and (box_pos.add_pos(Pos(0, 1)) not in all_boxes or ((vert) and depth == 1)) and (not box_pos.in_wall(self.walls) or depth == 1):
                return True

            if depth == 1 and box_pos not in all_boxes and box_pos.add_pos(Pos(0, -1)) in all_boxes and vert:
                box_pos = box_pos.add_pos(Pos(0, -1))
                
            if box_pos.in_wall(self.walls):
                return False
            
            box_poses: Set[WideBox] = set()
            if box_pos.add_pos(Pos(0, -1)) in all_boxes:
                box_ = box_pos.add_pos(Pos(0, -1)) 
                box_poses.add(box_)
                
            if box_pos in all_boxes:
                box_poses.add(box_pos)
            if depth > 1 and box_pos.add_pos(Pos(0, 1)) in all_boxes:
                box_poses.add(box_pos.add_pos(Pos(0, 1)))

            box_success = set()
            old2new = dict()
            for box_ in box_poses: 
                new_box = box_.add_pos(dir)
                success = move_box(new_box, dir, all_boxes - {box_}, depth + 1)
                box_success.add(success)
                old2new[box_] = new_box
    
            if all(box_success):
                for old_box_pos, new_box in old2new.items():
                    if old_box_pos in self.boxes:
                        self.boxes.remove(old_box_pos)
                    self.boxes.add(new_box)
                                
                return True

            return False
        
        if boxes is None:
            boxes = self.boxes 

        curr_robot_pos = self.robot + dir

        if curr_robot_pos in self.walls:
            print("Hit a wall")
            return
        
        curr_box = WideBox(curr_robot_pos)
        move = move_box(curr_box, dir, boxes)

        if move:
            self.robot = curr_robot_pos
    
def A(grid, moves):
    board = Board.from_grid(grid)
    
    pprint2d(board.grid)
    
    print(moves)
    
    for i, move in enumerate(moves):
        if move == '<':
            board.move_left()
        elif move == '^':
            board.move_up()
        elif move == '>':
            board.move_right()
        elif move == 'v':
            board.move_down()
        else:
            raise ValueError(f"Invalid move {move}")
        print("=" * 20, f"{i}th Move: {move}", "=" * 20)
        pprint2d(board.grid)
        print("=" * 50)
        print("=" * 50)
        # time.sleep(2)


    ansprint(board.GPS)
            
def B(grid, moves):
    board = WideBoard.from_grid(grid)
    
    pprint2d(board.grid)
    
    print(moves)
    
    for i, move in enumerate(moves):
        print("=" * 20, f"{i}th Move: {move}", "=" * 20)
        if move == '<':
            board.move_left()
        elif move == '^':
            board.move_up()
        elif move == '>':
            board.move_right()
        elif move == 'v':
            board.move_down()
        else:
            raise ValueError(f"Invalid move {move}")
        pprint2d(board.grid)
        print("=" * 50)
        # input()
        
    ansprint(board.GPS)

if __name__ == "__main__":
    grid, moves = load_file()
    B(grid, moves)