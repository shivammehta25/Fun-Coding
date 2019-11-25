
n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in range(1, 6):
    for j in range(n  - i + 1):
        subarr = a[j:j + i]
        if sum(subarr) % k == i:
            count += 1

print(count)
