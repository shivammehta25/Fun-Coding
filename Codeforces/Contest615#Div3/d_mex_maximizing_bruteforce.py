
def get_mex(arr):
    arr = sorted(list(set(arr)))
    perfect_arr = (i for i in range(len(arr)))
    for i in perfect_arr:
        if arr[i] != i:
            return i

    return arr[-1] + 1


n, x = map(int, input().split())
arr = []
for _ in range(n):
    i = int(input())
    arr.append(i)
    print(f"i : {i}")
    current_mex = get_mex(arr)
    if current_mex - i >= 3:

        current_mex = get_mex(arr[:-1] + [current_mex//3])
    print(current_mex)

print(arr, n, x)
