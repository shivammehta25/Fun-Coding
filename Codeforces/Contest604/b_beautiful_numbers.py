def check_arr(arr):
    arr = list(map(int,arr.split()))
    n = len(arr)
    if n == 1 :
        return '1'

    if n == 2:
        return '11'

    f_pos = arr.index(1)
    a = ['0' for _ in range(n)]
    a[0] = '1'
    a[-1] = '1'
    for i in range(2, n):
        l_range = max(0, f_pos - i + 1)
        r_range = min(n- 1, f_pos + i - 1)
        window_size = i
        ideal_array = [x for x in range(1, i+1)]
        for j in range(l_range, r_range - window_size + 2):
            if sorted(arr[j:j+window_size]) ==  ideal_array:
                a[i-1] = '1'
                break

    return ''.join(a)

n = int(input())
for _ in range(n):
    input()
    print(check_arr(input()))
