n = int(input())
array = list(map(int, input().strip().split()))
s = []
value = 0
d = {}
already_visited = set()
for i in array:
    value += 1
    if i > 0:
        if i not in d and i not in already_visited:
            d[i] = 1
        else:
            print(-1)
            exit(0)
    else:
        i = abs(i)
        if i not in d:
            print(-1)
            exit(0)
        else:
            already_visited.add(i)
            del d[i]

    if len(d) == 0:
        s.append(value)
        value = 0
        already_visited = set()

if len(d) == 0:
    print(len(s))
    print(' '.join(map(str, s)))
else:
    print(-1)
