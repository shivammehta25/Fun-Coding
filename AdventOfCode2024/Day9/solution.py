from pprint import pprint
from tqdm.auto import tqdm

log = False 
ansprint = print
if log:
    print = print
    pprint = pprint
else:
    print = lambda *x: None
    pprint = print

def load_file(path="dummy_inp.txt"):
    with open(path) as f:
        arr = f.readlines()
    
    arr = list(map(int, arr[0]))
    
    return arr


def get_new_arr(arr):
    id = 0
    arr_new = []
    num_dots = 0
    for i, v in enumerate(arr):
        if i & 1:
            arr_new.extend(['.' for _ in range(v)])
            num_dots += v
        else:
            arr_new.extend([id] * v)
            id += 1
    
    print("Num_dots: ", num_dots)
    
    return arr_new, num_dots

def A(arr):
    print(arr)
    
    arr_new, num_dots = get_new_arr(arr)
    
    l, r = 0, len(arr_new) - 1
    
    while l < r and r >= len(arr_new) - num_dots - 1:
        ansprint(f"\r {num_dots} l: {l} {arr_new[l]}, r: {r}, {arr_new[r]}", end="")
        if arr_new[l] != ".":
            l += 1
            continue
        if arr_new[r] == ".":
            r -= 1
            continue
        
        arr_new[l], arr_new[r] = arr_new[r], arr_new[l]

        r -= 1
        l += 1
        print("".join(map(str, arr_new)))
    
    print(arr_new)
    compute_checksum(arr_new)

def compute_checksum(arr_new):
    ans = 0
    for i, v in enumerate(arr_new):
        if v != ".":
            ans += i * v
    
    ansprint("")
    ansprint(ans)
    

def str_print(arr):
    if log:
        print("".join(map(str, arr)))

def find_repeating_nums(arr_new, r):
    while arr_new[r] == ".":
        r -= 1

    prev_r_val = arr_new[r]
    curr_r_count = 0
    while r >= 0 and prev_r_val == arr_new[r]:
        if arr_new[r] == ".":
            break
        # arr_new[r] = "."

        r -= 1
        curr_r_count += 1
    
    return r + 1, curr_r_count, prev_r_val
    
    
def find_suitable_dots(arr_new, curr_r_count, l=0):
    if l >= len(arr_new):
        return -1

    while l < len(arr_new) and arr_new[l] != ".":
        l += 1

    curr_dot_count = 0
    while l < len(arr_new):
        if arr_new[l] == ".":
            curr_dot_count += 1
        else:
            break
        
        l += 1 
        
    if curr_dot_count >= curr_r_count:
        return l - curr_dot_count
    else:
        l = find_suitable_dots(arr_new, curr_r_count, l)

    return l


def find_suitable_dots_itr(arr_new, curr_r_count):
    n = len(arr_new)
    curr_dots = 0
    for i in range(n + 1):
        if i == n:
            break

        if arr_new[i] != ".":
            if curr_dots >= curr_r_count:
                break
            else:
                curr_dots = 0
                continue
        curr_dots += 1
    return i - curr_dots

    
def B(arr):
    arr_new, num_dots = get_new_arr(arr)
    str_print(arr_new)
    r =len(arr_new) - 1
    curr_r_count = 0
    while r > 0 and num_dots > 0:
        # ansprint(f"\r {num_dots} l: {l} {arr_new[l]}, r: {r}, {arr_new[r]}", end="")
        r, curr_r_count, prev_r_val = find_repeating_nums(arr_new, r)
        to_move_r = r 
        print(f"r: {r}, curr_r_count: {curr_r_count}, prev_r_val: {prev_r_val}")
        print(f"num_dots: {num_dots}")
        
        l = find_suitable_dots_itr(arr_new, curr_r_count)
        print(f"suitable l: {l}")

        str_print(arr_new)
        print(f"{' ' * (l)}l{' ' * (r - l - 1)}r")
        if l  == -1 or l > r:
            r -= 1
            continue

        for i in range(curr_r_count):
            arr_new[l + i] = prev_r_val
            arr_new[to_move_r + i] = "."
            num_dots -= 1
            
        r -= 1
        ansprint(f"\r{r}", end="")
        
    compute_checksum(arr_new)
    

if __name__ == "__main__":
    arr = load_file("inp.txt")
    B(arr)

    # t = [".", 1, 2, 3, ".", ".", 4, 4, 5, ".", ".", ".", 6]
    # print(find_suitable_dots_itr(t, 3))
