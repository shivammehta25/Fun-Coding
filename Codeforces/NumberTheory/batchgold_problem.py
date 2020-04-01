# https://codeforces.com/problemset/problem/749/A


n = int(input())

if n & 1:
    if n == 3:
        print("1\n3")
    else:
        print(n // 2)
        print("{} 3".format(" ".join(["2" for i in range(n // 2 - 1)])))
else:
    if n == 2:
        print("1\n2")
    else:
        print(n // 2)
        print(" ".join(["2" for i in range(n // 2)]))
