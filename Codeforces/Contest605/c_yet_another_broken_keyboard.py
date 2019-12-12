n, k_l = map(int, input().split())
string = input()
keyboard = input().split()

string = ''.join([i if i in keyboard else ';^;' for i in string])
count = 0
for s in string.split(';^;'):
    n = len(s)
    count += (n * (n + 1)) // 2

print(count)
