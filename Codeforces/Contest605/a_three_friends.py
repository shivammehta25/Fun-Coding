n = int(input())


def do_operation(a, avg):
    if a >= avg:
        if a != avg:
            a -= 1
    else:
        a += 1

    return a


def reduce_min_sum(a):
    for _ in range(2):
        if a == 0:
            break
        a -= 1
    return a


def get_min_pariwise(a, b, c):
    arr = [a, b, c]
    avg = (max(arr) + min(arr)) // 2
    a = do_operation(a, avg)
    b = do_operation(b, avg)
    c = do_operation(c, avg)
    s = 0
    s += (abs(a - b))
    s += (abs(b - c))
    s += (abs(c - a))

    return s


for _ in range(n):
    a, b, c = map(int, input().split())
    print(get_min_pariwise(a, b, c))
