


def solve(n):
    count = 0 # 0
    n_coins = 1 # 1
    while n > 3: 
        # count += 1 if (n % 4) != 0 else 0
        n //= 4
        n_coins *= 2 

    print(n_coins + count)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        solve(int(input()))