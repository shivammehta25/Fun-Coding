from collections import defaultdict
from pprint import pprint

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
        print("".join(map(str, x)))

def load_file(path="dummy_inp.txt"):
    with open(path) as f:
        arr = f.readlines()
    
    arr = [[int(x) if str.isdigit(x) else x for x in row.strip()] for row in arr]
    
    return arr


def A(arr):
    
    m = len(arr)
    n = len(arr[0])
    
    pprint2d(arr) 
    def find_trail(arr, i, j, val, orig_i, orig_j, reached_9):
        if arr[i][j] != val or val > 9:
            return

        if arr[i][j] == 9:
            reached_9.add((i, j))
        
        for x, y in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = i + x, j + y
            if 0 <= new_x < m and 0 <= new_y < n:
                find_trail(arr, new_x, new_y, val + 1, orig_i, orig_j, reached_9)

    ans = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                reached_9 = set()
                find_trail(arr, i, j, arr[i][j], i, j, reached_9)
                print(i, j, reached_9)
                ans += len(reached_9)
    
    ansprint()
    ansprint(ans)
    
def B(arr):
    m = len(arr)
    n = len(arr[0])
    
    pprint2d(arr) 
    all_trails = defaultdict(int)
    def find_trail(arr, i, j, val, orig_i, orig_j):
        if arr[i][j] != val or val > 9:
            return

        if arr[i][j] == 9:
            all_trails[(orig_i, orig_j)] += 1
        
        for x, y in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = i + x, j + y
            if 0 <= new_x < m and 0 <= new_y < n:
                find_trail(arr, new_x, new_y, val + 1, orig_i, orig_j)

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                find_trail(arr, i, j, arr[i][j], i, j)

    ansprint()
    ansprint(sum(all_trails.values())) 


if __name__ == "__main__":
    arr = load_file("inp.txt")
    B(arr)
