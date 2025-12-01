import re
import sys
from dataclasses import dataclass
from functools import cache
from pprint import pprint

log = True 
ansprint = print

digit_pattern = re.compile(r'\d+') 

@dataclass
class Pos:
    X: int
    Y: int

    
    def __add__(self, other: "Pos") -> "Pos":
        return Pos(self.X + int(other.X), self.Y + int(other.Y))

    def __eq__(self, other: "Pos") -> bool:
        return self.X == int(other.X) and self.Y == int(other.Y)
    
    def __repr__(self) -> str:
        return f"({self.X}, {self.Y})"
    
    def __gt__(self, other: "Pos") -> bool:
        if self.X > int(other.X) or self.Y > int(other.Y):
            return True
        
        return False
    
    def __hash__(self) -> int:
        return hash((self.X, self.Y))
            


class Machine:
    def __init__(self, button_A, button_B, prize) -> None:
        self.A = button_A
        self.B = button_B
        self.prize = prize
    
    @classmethod
    def from_lines(cls, lines, offset=0):
        x_a, y_a = digit_pattern.findall(lines[0])
        x_b, y_b = digit_pattern.findall(lines[1])
        x_p, y_p = digit_pattern.findall(lines[2])
        return cls(Pos(int(x_a), int(y_a)), Pos(int(x_b), int(y_b)), Pos(int(x_p), int(y_p)))
    
    def update_prize(self, offset=10000000000000):
        self.prize.X += int(offset)
        self.prize.Y += int(offset)

    def __repr__(self) -> str:
        return f"[A: {self.A}, B: {self.B}, Prize: {self.prize}]"


if not log:
    print = lambda *x: None
    pprint = print
    
def pprint2d(arr):
    for x in arr:
        print("".join(map(str, x)))

def load_file():
    lines = [x.strip() for x in sys.stdin]
    
    arr = []
    for i in range(0, len(lines), 4):
        arr.append(Machine.from_lines(lines[i: i + 4]))

    print(f"Loaded {len(arr)} machines.")
    return arr


def A(arr):
    
    @cache
    def recursive_soln(machine, curr_pos=Pos(0, 0), curr_cost=0, count_a=0, count_b=0):
        # print(curr_pos, machine.prize, curr_pos > machine.prize, "count:", "a", count_a, "b", count_b)
        if count_a > 100 or count_b > 100 or curr_pos > machine.prize:
            return float("inf"), count_a, count_b

        elif curr_pos == machine.prize:
            return curr_cost, count_a, count_b

        else:
            a_curr_cost, a_count_a, a_count_b = recursive_soln(machine, curr_pos + machine.A, curr_cost + 3, count_a + 1, count_b)
            b_curr_cost, b_count_a, b_count_b = recursive_soln(machine, curr_pos + machine.B, curr_cost + 1, count_a, count_b + 1)
            
            if a_curr_cost <= b_curr_cost:
                return a_curr_cost, a_count_a, a_count_b
            else:
                return b_curr_cost, b_count_a, b_count_b

    ans = 0
    for machine in arr:
        cost, a_count, b_count = recursive_soln(machine)
        print(cost, a_count, b_count)
        if cost != float("inf"):
            ans += cost
    
    ansprint() 
    ansprint(ans)


def solve_system_of_eq(machine):
        ax, ay = machine.A.X, machine.A.Y
        bx, by = machine.B.X, machine.B.Y
        px, py = machine.prize.X, machine.prize.Y

        # Simply Using cramers formula
        n1 = (px*by - py*bx) / (ax*by - ay*bx)
        n2 = (py*ax - px*ay) / (ax*by - ay*bx)

        return n1, n2

def A_system(arr):
    
    ans = 0
    for machine in arr:
        n1, n2= solve_system_of_eq(machine)
        print(n1, n2)
        if int(n1) == n1 and int(n2) == n2 and int(n1) > 0 and int(n2) > 0:
            ans += 3 * n1 + 1 * n2
    
    ansprint() 
    ansprint(ans) 
    
    
    

def B(arr):
    for a in arr:
        a.update_prize()
        
    ans = 0
    for machine in arr:
        n1, n2= solve_system_of_eq(machine)
        print(n1, n2)
        if int(n1) == n1 and int(n2) == n2 and int(n1) > 0 and int(n2) > 0:
            ans += 3 * n1 + 1 * n2
    
    ansprint() 
    ansprint(int(ans))


if __name__ == "__main__":
    arr = load_file()
    B(arr)