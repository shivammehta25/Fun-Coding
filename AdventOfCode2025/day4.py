from utils import Input, print_2d

day = 4


def run_forklift(grid: list[list[str]], replace_x=False) -> tuple[int, list[list[str]]]:
    ajd_loc = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x != 0 or y != 0] 

    MAX_ADJ_COUNT = 4
    ans = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '.':
                continue
            
            curr_adj_count = 0
            for x, y in ajd_loc:
                if 0 <= i + x < len(grid) and 0 <= j + y < len(row):
                    if grid[i + x][j + y] != '.':
                        curr_adj_count += 1
                    
            if curr_adj_count < MAX_ADJ_COUNT:
                ans += 1
                grid[i][j] = 'x'
    
    if replace_x:
        grid = [[x if x != 'x' else '.' for x in row] for row in grid]
    
    return ans, grid


def A():
    input = Input(day, 'a').convert_to_2d()
    INPUT = input.data
    ans, grid = run_forklift(INPUT)
    print(f"{ans=}")
            

def B():
    input = Input(day, 'a').convert_to_2d()
    INPUT = input.data
    grid = INPUT
    ans = 0
    curr_round = -1
    rounds = 0

    while curr_round != 0:
        curr_round, grid = run_forklift(grid, replace_x=True)
        ans += curr_round
        rounds += 1
    
    print(f"{ans=}, {rounds=}")

    

if __name__ == '__main__':
    A()
    print("-" * 50)
    B()
