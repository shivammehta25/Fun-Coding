def merge_sort(a):
    inv_count = 0
    N = len(a)
    if N >= 2:
        inversion, left = merge_sort(a[:N//2])
        inv_count += inversion
        inversion, right = merge_sort(a[N//2:])
        inv_count += inversion
        inversion, a = merge(left, right)
        inv_count += inversion
        
    return inv_count, a

def merge(left, right):
    _aux = []
    inv_count = 0
    L = len(left)
    R = len(right)
    i, j = 0, 0
    while i < L and j < R:
        if left[i] <= right[j]:
            _aux.append(left[i])
            i += 1
        else:
            _aux.append(right[j])
            inv_count += len(left[i:])
            j += 1

    print(inv_count, left, right)
    _aux.extend(left[i:])
    _aux.extend(right[j:])
    
    return  inv_count, _aux
    
    


def count_inversion(a, n):
    return merge_sort(a)



t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(count_inversion(a, n))
