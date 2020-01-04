n = int(input())
for _ in range(n):
    h, m = map(int, input().split())
    print((60 - m) + (23 - h) * 60)
