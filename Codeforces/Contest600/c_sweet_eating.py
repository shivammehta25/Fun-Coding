# TLE : Read Greedy Algorithms

n, m = map(int, input().strip().split())
a = list(map(int, input().split()))
a = sorted(a)
ans = []
for i in range(n):
    multiplier = 1
    sum_of_sugar = 0
    multi_checker = 0
    for j in range(i, -1, -1):
        sum_of_sugar += multiplier * a[j]
        multi_checker += 1
        if multi_checker % m == 0:
            multiplier += 1
    ans.append(sum_of_sugar)

print(' '.join(map(str, ans)))
