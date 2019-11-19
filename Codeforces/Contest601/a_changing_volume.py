def change_volume(a, b):
    if a==b:
        return 0

    sum = 0
    diff = abs(a-b)
    sum += diff//5
    diff %= 5
    sum += diff//2
    diff %= 2
    sum += diff
    return sum



n = int(input())
for _ in range(n):
    a, b = map(int, input().strip().split())
    print(change_volume(a, b))
