from pprint import pprint
from itertools import cycle
log = True

if log:
    print = print
    pprint = pprint
else:
    print = lambda x: None
    pprint = print


def load_file(path="dummy_inp.txt"):
    with open(path) as f:
        arr = f.readlines()
    
    arr = [[x for x in row.strip()] for row in arr]
    
    return arr

def find_start_coordinates(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != "#" and arr[i][j] != ".":
                return i, j
    

def in_bound(val, len_arr):
    return 0 <= val < len_arr


def A(arr):
    # pprint(arr)
    m = len(arr)
    n = len(arr[0])
    curr_x, curr_y = find_start_coordinates(arr)
    # print(arr[curr_x][curr_y])
    ptr = arr[curr_x][curr_y]
    direction = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1)
    }
    next_dir = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^"
    }
    count = 0
    while in_bound(curr_x, m) and in_bound(curr_y, n):
        if arr[curr_x][curr_y] == ptr:
            arr[curr_x][curr_y] = "X"
            count += 1

        delta_x, delta_y = direction[ptr]
        if in_bound(curr_x + delta_x, m) and in_bound(curr_y + delta_y, n):
            if arr[curr_x + delta_x][curr_y + delta_y] == "#":
                ptr = next_dir[ptr]
                delta_x, delta_y = direction[ptr]
            if arr[curr_x + delta_x][curr_y + delta_y] != "X":
                arr[curr_x + delta_x][curr_y + delta_y] = ptr
                
                 
        
        curr_x += delta_x
        curr_y += delta_y
        
        pprint(arr)
        print(count)
        input()
        

def B(arr):
    # pprint(arr)
    m = len(arr)
    n = len(arr[0])
    curr_x, curr_y = find_start_coordinates(arr)
    # print(arr[curr_x][curr_y])
    ptr = arr[curr_x][curr_y]
    direction = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1)
    }
    next_dir = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^"
    }
    count = 0
    while in_bound(curr_x, m) and in_bound(curr_y, n):
        if arr[curr_x][curr_y] == ptr:
            arr[curr_x][curr_y] = "X"
            count += 1

        delta_x, delta_y = direction[ptr]
        if in_bound(curr_x + delta_x, m) and in_bound(curr_y + delta_y, n):
            if arr[curr_x + delta_x][curr_y + delta_y] == "#":
                ptr = next_dir[ptr]
                delta_x, delta_y = direction[ptr]
            if arr[curr_x + delta_x][curr_y + delta_y] != "X":
                arr[curr_x + delta_x][curr_y + delta_y] = ptr
                
                 
        
        curr_x += delta_x
        curr_y += delta_y
        
        # pprint(arr)
        print(count)
        # input()
        
        

        

    
    
    
    


if __name__ == "__main__":
    arr = load_file()
    A(arr)