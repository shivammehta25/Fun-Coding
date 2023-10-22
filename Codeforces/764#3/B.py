from itertools import permutations

def solve():
    arr = list(map(int, input().split()))
    print(list(permutations(arr, 2)))

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        solve()
