import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = n // k
    n_a = k // 2 if not k % 2 else (k // 2) + 1
    n_b = k - n_a
    print(min((a * n_a) + ((a + 1) * n_b), n))
