# https://atcoder.jp/contests/abc148/tasks/abc148_b
string = []
n = int(input())
a, b = input().split()
for i in range(n):
    string.append(a[i])
    string.append(b[i])

print(''.join(string))
