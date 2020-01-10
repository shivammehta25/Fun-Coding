n = int(input())

if n & 1:
    print(0)
    exit(0)

n //= 2
ans = 0
while n:
    ans += (n // 5)
    n //= 5

print(ans)
