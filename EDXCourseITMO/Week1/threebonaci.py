#!/usr/bin/env python3

with open('input.txt', 'r') as input:
    a0, a1, a2, n = [int(x) for x in input.readline().split(' ')]


# def fibo(i):
#     if i == 0:
#         return a0
#     elif i == 1:
#         return a1
#     elif i == 2:
#         return a2
#     else:
#         return fibo(i-1) + fibo(i-2) - fibo(i-3)

def fibo(n):
    a = [0] * (n+1)
    a[0] = a0
    if n < 1:
        return a[0]
    a[1] = a1
    if n < 2:
        return a[1]
    a[2] = a2
    for i in range(3, n+1):
        a[i] = a[i-1] + a[i-2] - a[i-3]
    print(a)
    return a[n]


with open('output.txt', 'w') as output:
    output.write(str(fibo(n)))
    output.write('\n')
