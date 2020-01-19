x = int(input())

if x == 1 or x == 2:
    print('1 {}'.format(x))
    exit()


def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def lcm(x, y):
    return x*y // compute_gcd(x, y)


ans = 0
for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0 and lcm(i, x//i) == x:
        ans = i

print('{} {}'.format(ans, x//ans))
