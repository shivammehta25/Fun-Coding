t = int(input())


def find_one_factor(num, a):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if a == i:
                continue
            return i, num // i

    return -1, -1


while t:
    t -= 1
    n = int(input())
    flag = True
    factors = []

    a, num = find_one_factor(n, 0)
    if a == -1:
        print("NO")
        continue
    b, num = find_one_factor(num, a)
    if b == -1:
        print("NO")
        continue
    elif b == num:
        print("NO")
        continue

    c = num

    print("YES")
    print("{} {} {}".format(a, b, c))

