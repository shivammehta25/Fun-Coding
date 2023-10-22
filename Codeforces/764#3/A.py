def solve():
    _ = int(input())
    arr = list(map(int, input().split()))
    print(max(arr)- min(arr))


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        solve()
