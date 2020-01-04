n = int(input())
a = list(map(int, input().split()))
s = [False] * (n)
r = [False] * (n)


for i in range(n):
    if a[i]:
        s[i] = True
        r[a[i] - 1] = True

a = [i - 1 if i else 0 for i in a]

s_ = []
r_ = []


for i in range(len(s)):
    if not s[i]:
        s_.append(i)

    if not r[i]:
        r_.append(i)

s = s_
r = r_


for i in range(len(s)):
    if s[i] == r[i]:
        if i == 0:
            r[i], r[i+1] = r[i+1], r[i]
        else:
            r[i], r[i-1] = r[i-1], r[i]

for i in range(len(s)):
    a[s[i]] = r[i]


for i in range(len(a)):
    a[i] = a[i] + 1


print(' '.join(map(str, a)))
