# https://www.geeksforgeeks.org/toggling-k-th-bit-number/


inp, k = map(int, input().split())

i = 0
print((1 << k - 1) ^ inp)

