def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


x, y = map(int, input().split())

print(x*y // gcd(x, y))
