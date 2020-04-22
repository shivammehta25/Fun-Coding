t = int(input())

while t:
    t -= 1

    n = int(input())
    arr = list(map(int, input().split()))

    current = arr[0]

    i = 1
    max_sum = 0

    

    while i < len(arr):
        if current * arr[i] >= 0:
            current = max(current, arr[i])
        else:
            max_sum += current
            current = arr[i]
        
        i += 1

    max_sum += current

    print(max_sum)
