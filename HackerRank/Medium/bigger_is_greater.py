# https://www.hackerrank.com/challenges/bigger-is-greater/problem

def char_to_int(arr):
    dicty = { chr(i + 96): i for i in range(1, 27)}
    return [dicty[i] for i in arr]

def int_to_char(arr):
    dicty = {i: chr(i+96) for i in range(1, 27)}
    return [dicty[i] for i in arr]


def next_permutation(arr):
    arr = char_to_int(arr)
    N = len(arr) - 1
    p = N
    while p >= 0 and arr[p-1] >= arr[p]:
        p -= 1
    if p <= 0:
        return 'no answer'

    p = p - 1
    swapper = N
    while arr[swapper] <= arr[p]:
        swapper -= 1
    arr[swapper], arr[p] = arr[p], arr[swapper]
    arr[p+1:] = arr[N:p:-1]
    
    
    return ''.join(int_to_char(arr))

for _ in range(int(input())):
    print(next_permutation(input()))
