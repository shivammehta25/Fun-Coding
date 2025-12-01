import re
import sys
from pprint import pprint

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
            if l == 0:
                row.append('.')
            else:
                row.append(str(l))        
        print("".join(row))



digit_re = re.compile(r'\-*\d+')

def parse_line(line):
    posX, posY, Vx, Vy = digit_re.findall(line)
    return int(posX), int(posY), int(Vx), int(Vy)


def load_file():
    lines = [parse_line(x.strip()) for x in sys.stdin]
    print(f"Loaded {len(lines)} swarms.")
    return lines


def get_state(init_x, init_y, v_x, v_y, time, m, n):
    pos_x, pos_y = v_x * time, v_y * time
    return (init_x + pos_x) % m, (init_y + pos_y) % n

def compute_quadrant_sum(grid):
    n = len(grid)
    m = len(grid[0])

    quadrants = {1: 0, 2: 0, 3: 0, 4: 0} 
    
    for i in range(n):
        for j in range(m):
            if i == n // 2 or j == m // 2:
                continue
            
            if i < n // 2 and j < m // 2:
                quadrant = 1
            elif i > n // 2 and j < m // 2:
                quadrant = 3
            elif i < n // 2 and j > m // 2:
                quadrant = 2
            else:
                quadrant = 4
            
            quadrants[quadrant] += grid[i][j]
    
    ans = 1
    
    for k, v in quadrants.items():
        ans *= v
    
    return ans
    
def in_lim(x, max_val):
    return 0<= x < max_val

def get_neighbourhood(arr ,orig_i, orig_j):
    m = len(arr)
    n = len(arr[0])
    
    neighbours = [['.'] * 3 for _ in range(3)]
    for i, x in enumerate([-1, 0, 1]):
        for j, y in enumerate([-1, 0, 1]):
            n_x, n_y = orig_i + x, orig_j + y
            if in_lim(n_x, m) and in_lim(n_y, n):
                neighbours[i][j] = arr[n_x][n_y]
    
    return neighbours

def B(arr):
    # m, n = 101, 103
    
    # max_time = 10
    
    # for t in range(max_time):
    #     grid = [[0] * m for _ in range(n)]
        
    #     for swarm_i in arr:
    #         curr_x, curr_y = get_state(*swarm_i, t,  m, n)
    #         grid[curr_y][curr_x] += 1

    #     print(t)
    #     pprint2d(grid)
    #     print("=" * 100)

    max_time = 10000
    max = -1
    min_ = float("inf")
    for t in range(max_time): 
        ans, grid = A(arr, t, False)
        if ans >= max:
            print("Max")
            print(t, ans)
            pprint2d(grid)
            max = ans
        if ans < min_:
            print("Min")
            print(t, ans)
            pprint2d(grid)
            min_ = ans
            


def A(arr, t=100, print_it=True):
    m, n = 101, 103
    
    grid = [[0] * m for _ in range(n)]
    

    for swarm_i in arr:
        curr_x, curr_y = get_state(*swarm_i, t,  m, n)
        grid[curr_y][curr_x] += 1
    
    ans = compute_quadrant_sum(grid)
    if print_it:
        ansprint(t, ans)
    
    return ans, grid


if __name__ == "__main__":
    arr = load_file()
    B(arr)