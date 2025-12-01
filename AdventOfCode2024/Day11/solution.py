from functools import cache
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
    
    arr = list(map(int, arr[0].split()))
    
    return arr


def blink(stone):
    next_ = []
    n = stone
    if n == 0:
        next_.append(1)
    elif len(str(n)) & 1 == 0:
        n = str(n)
        a, b = n[:len(n) // 2], n[len(n) // 2:]
        next_.append(int(a))
        next_.append(int(b))
    else:
        next_.append(n * 2024)

    return next_

@cache
def compute(stone, blink_num):
    next_step = blink(stone)
    if blink_num == 1:
        return len(next_step)
    
    ans = 0
    for ns in next_step:
        ans += compute(ns, blink_num - 1)

    return ans


def A(arr, n_blinking=25):
    ans = 0
    for stone in tqdm(arr):
        ans += compute(stone, n_blinking)        
    
    ansprint()
    ansprint(ans)
        
def B(arr):
    A(arr, 75)

if __name__ == "__main__":
    arr = load_file("inp.txt")
    B(arr)