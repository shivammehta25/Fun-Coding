t = int(input())

while t:
    n = int(input())
    k = 2
    while True:
        x = n / (2**k - 1)
        if int(x) == x:
            print(int(x))
            break
        k += 1

    t -= 1
