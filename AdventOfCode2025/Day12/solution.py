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
    
    arr = [[x for x in row.strip()] for row in arr]
    
    return arr
    


def compute_ans(area, perimeter):
    return sum([v1 * v2 for (k, v1), (k, v2) in zip(area.items(), perimeter.items())])
    



        

def A(arr):
    def make_unique_islands(arr):
        n = len(arr)
        m = len(arr[0])
        
        curr_num = 0
        
        for i in range(n):
            for j in range(m):
                if not str.isdigit(str(arr[i][j])):
                    dfs(arr, i, j, arr[i][j], curr_num)
                    curr_num += 1
                    
    def dfs(arr, i, j, orig_val, curr_num):
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]) or arr[i][j] != orig_val:
            return

        arr[i][j] = curr_num
        dfs(arr, i + 1, j, orig_val, curr_num)
        dfs(arr, i - 1, j, orig_val, curr_num)
        dfs(arr, i, j + 1, orig_val, curr_num)
        dfs(arr, i, j - 1, orig_val, curr_num)
        
    def compute_perimeter(arr, i, j):
        m = len(arr)
        n = len(arr[0])
        curr_perimeter = 4
        curr_element = arr[i][j]
        
        for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_i, new_j = i + delta_x, j + delta_y
            if 0 <= new_i < m and 0 <= new_j < n and arr[new_i][new_j] == curr_element:
                curr_perimeter -= 1
        
        return curr_perimeter
                    
    make_unique_islands(arr)
    pprint(arr)    
    
    area = defaultdict(int)
    perimeter = defaultdict(int)
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        for j in range(m):
            area[arr[i][j]] += 1
            perimeter[arr[i][j]] += compute_perimeter(arr, i, j)

    pprint(area)
    pprint(perimeter)

    ansprint(compute_ans(area, perimeter))
    
    
def B(arr):
    
    def make_unique_islands(arr):
        n = len(arr)
        m = len(arr[0])
        
        curr_num = 0
        
        for i in range(n):
            for j in range(m):
                if not str.isdigit(str(arr[i][j])):
                    dfs(arr, i, j, arr[i][j], curr_num)
                    curr_num += 1

    location = defaultdict(list)

    def dfs(arr, i, j, orig_val, curr_num):
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]) or arr[i][j] != orig_val:
            if 0 <= i < len(arr) and 0 <= j < len(arr) and arr[i][j] == curr_num:
                return
                
            # edges[curr_num].append((i, j))
            return

        arr[i][j] = curr_num
        location[curr_num].append((i, j))
        
        dfs(arr, i + 1, j, orig_val, curr_num)
        dfs(arr, i - 1, j, orig_val, curr_num)
        dfs(arr, i, j + 1, orig_val, curr_num)
        dfs(arr, i, j - 1, orig_val, curr_num)
    
       
    def compute_corners(arr):
        
        count = 0
        curr_val = arr[1][1]
        top_left_corner = [(0, 1), (1, 0)]
        top_right_corner = [(0, 1), (1, 2)]
        bottom_left_corner = [(1, 0), (2, 1)]
        bottom_right_corner = [(2, 1), (1, 2)]
        
        
        for corner in [top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner]:
            if arr[corner[0][0]][corner[0][1]] != curr_val and arr[corner[1][0]][corner[1][1]] != curr_val:
                count += 1
                
        convex_inner_bottom_right = [(2, 1), (1, 2), [2, 2]]
        convex_inner_bottom_left = [(1, 0), (2, 1), [2, 0]]
        convex_inner_up_left = [(1, 0), (0, 1), [0, 0]]
        convex_inner_up_right =  [(0, 1), (1, 2), [0, 2]]
        
        for corner in [convex_inner_bottom_right, convex_inner_bottom_left, convex_inner_up_left, convex_inner_up_right]:
            if arr[corner[0][0]][corner[0][1]] == curr_val and arr[corner[1][0]][corner[1][1]] == curr_val and arr[corner[2][0]][corner[2][1]] != curr_val:
                count += 1
        
        return count
    
    make_unique_islands(arr)
    
    area = defaultdict(int)
    n = len(arr)
    m = len(arr[0])
    
    pprint2d(arr)
    
    corners = defaultdict(int)
    for i in range(n):
        for j in range(m):
            area[arr[i][j]] += 1
            
            neighbours = get_neighbourhood(arr, i, j)
            print(i, j)
            pprint2d(neighbours)
            corner_count = compute_corners(neighbours)
            corners[arr[i][j]] += corner_count
            print("curr_val: ", arr[i][j], "corner_count: ", corner_count)
            

    pprint(area)
    pprint2d(arr)
    pprint(location)

    pprint(corners)

    ansprint(compute_ans(area, corners))



def plot_edges(edges, n, m):

    for edge, v in edges.items():
        arr = [[0] * (m + 2)  for _ in range(n + 2)]
        for (a, b) in v:
            print(arr[a + 1][b + 1])
            arr[a + 1][b + 1] = edge + 1

        pprint2d(arr)
    
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

def in_lim(x, max_val):
    return 0<= x < max_val


if __name__ == "__main__":
    arr = load_file("inp.txt")
    B(arr)
