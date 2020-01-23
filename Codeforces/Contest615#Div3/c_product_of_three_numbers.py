def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


t = int(input())
while t:
    t -= 1
    n = int(input())
    flag = True
    factors = []
    i = 2

    if is_prime(n):
        print('NO')
        continue

    while n > 0:
        if not is_prime(n) and len(factors) < 2:
            if i <= n:
                if n % i == 0:
                    factors.append(i)
                    n //= i
                i += 1
            elif len(factors) == 2 and n >= 2:
                factors.append(n)
                break
            else:
                print('NO')
                flag = False
                break

        elif len(factors) == 2:
            factors.append(n)
            break
        else:
            print('NO')
            flag = False
            break

    if len(set(factors)) != 3 and flag:
        print('NO')
        flag = False

    if flag:
        print('YES')
        print('{} {} {}'.format(factors[0], factors[1], factors[2]))
