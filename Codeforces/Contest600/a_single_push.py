
def check_it(a, b, size):
    k = 0
    input_time = 0
    k_stack = []
    for i in range(size):
        if a[i] > b[i]:
            return 'NO'
        elif a[i] == b[i]:
            if k_stack:
                k_stack.pop()
            continue
        else:
            k = b[i] - a[i]
            if not k_stack:
                k_stack.append(k)
                input_time += 1
            else:
                if k_stack[-1] == k:
                    continue
                else:
                    return 'NO'
        if input_time > 1:
            return 'NO'

    return 'YES'



n = int(input())
for i in range(n):
    x = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    print(check_it(a, b, x))
