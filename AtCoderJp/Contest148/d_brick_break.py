n = int(input())
a = list(map(int, input().split()))
i = 1
broken = 0
found = False
for v in a:
    if i == v:
        i += 1
        found = True
    else:
        broken += 1

if found:
    print(broken)
else:
    print(-1)
