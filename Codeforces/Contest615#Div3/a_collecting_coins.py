t = int(input())
while t:
    t -= 1
    a, b, c, n = map(int, input().split())
    m = max([a, b, c])
    s = 0
    for x in [a, b, c]:
        if x == m:
            continue
        s += m - x

    if n - s >= 0 and (n - s) % 3 == 0:
        print("YES")
    else:
        print("NO")
