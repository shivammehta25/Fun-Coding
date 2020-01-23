def get_answer():
    n = int(input())
    arr = [(0, 0)]
    for i in range(n):
        arr.append(tuple(map(int, input().split())))

    arr = sorted(arr, key=lambda element: (element[0], element[1]))
    dis_array = []
    for i in range(1, len(arr)):
        x2, y2 = arr[i]
        x1, y1 = arr[i - 1]
        dis_array.append(((x2 - x1), (y2 - y1)))

    answer = []
    for x, y in dis_array:
        if x < 0 or y < 0:
            return 'NO', ''
        s1 = 'R' * x
        s2 = 'U' * y
        answer.append(s1)
        answer.append(s2)

    return 'YES', ''.join(answer)


t = int(input())
while t:
    t -= 1
    s, ans = get_answer()
    print(s)
    if s == 'YES':
        print(ans)
