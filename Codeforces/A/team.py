# https://codeforces.com/problemset/problem/231/A

n = int(input())
total_count = 0
for _ in range(n):
    a = input().split('1')
    if len(a) > 2:
        total_count += 1

print(total_count)
