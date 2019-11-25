a, b, x = map(int, input().split())
n = 0
while True:
    n += 1
    if (a * n + b * len(str(n)) < x):
        continue
    else:
        n -= 1
        break

print(max(0, n))
