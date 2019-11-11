from itertools import compress


def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    factors = [1 for _ in range(n + 1)]
    p = 3
    max_number = 0
    max_index = 0
    while (p <= n):
        for i in range(p, n + 1, p):
            factors[i] += 1

        if factors[p] > max_number:
            max_number = factors[p]
            max_index = p
        p += 1
    print(n, factors)
    return max_index

    # sieve = bytearray([True]) * (n // 2)
    # for i in range(3, int(n ** 0.5) + 1, 2):
    #     if sieve[i // 2]:
    #         sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    # print(sieve)

with open('input.txt', 'r') as input:
    N = int(input.readline())
    max_number = primes(N)
    max_test = N + 1 - max_number
    print(max_test)
with open('output.txt', 'w') as output:
    output.write(str(max_test))
    output.write('\n')



# 12 [1, 2, 4, 3, 6, 12]
# 13 [1, 13]
# 14 [1, 2, 7, 14]
# 15 [1, 3, 5, 15]
# 16 [1, 2, 4, 8, 16]
# 17 [1, 17]
# 18 [1, 2, 3, 6, 9, 18]
# 19 [1, 19]
# 20 [1, 2, 4, 5, 10, 20]
# 21 [1, 3, 7, 21]
# 22 [1, 2, 11, 22]
# 23 [1, 23]
# 24 [1, 2, 4, 8, 3, 6, 12, 24]
# 24 : maxNumber : 24, maxTest: 1





# with open('input.txt', 'r') as input:
#     N = int(input.readline())
#     max_divisors = -1
#     max_number = 0
#     for x in range(1, N+1):
#         divisors = {1}
#         for y in range(2, int(sqrt(x)) + 1):
#             if x % y == 0:
#                 divisors.update({y, x//y})
#         divisors.add(x)
#         if len(divisors) > max_divisors:
#             max_divisors = len(divisors)
#             max_number = x
#     max_test = N + 1 - max_number
# with open('output.txt', 'w') as output:
#     output.write(str(max_test))
#     output.write('\n')
