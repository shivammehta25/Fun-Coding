from math import sqrt
from itertools import compress

def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def factorization(n):
    """ Returns a list of the prime factorization of n """
    pf = []
    primeslist = primes(int(n**0.5)+1)
    for p in primeslist:
        if p*p > n:
            break
        count = 0
        while not n % p:
            n //= p
            count += 1
        if count > 0:
            pf.append((p, count))
    if n > 1:
        pf.append((n, 1))

    return pf

def divi(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in factorization(n):
        divs += [x*p**k for k in range(1, e+1) for x in divs]
    return divs

with open('input.txt', 'r') as input:
    N = int(input.readline())
    max_divisors = -1
    max_number = 0
    x = N//2
    while x < N+1:
    # for x in range(N//2, N+1):
        divisors = divi(x)
        # print(x, divisors)
        if len(divisors) > max_divisors:
            max_divisors = len(divisors)
            max_number = x
        x += 1
    max_test = N + 1 - max_number
with open('output.txt', 'w') as output:
    output.write(str(max_test))
    output.write('\n')








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
