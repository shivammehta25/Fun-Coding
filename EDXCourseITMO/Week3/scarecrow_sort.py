
def determine_to_be_sorted(a, n, k):
    for j in range(k):
        a[j::k] = sorted(a[j::k])


    i = 0
    while i < n - 2:
        
        if a[i] > a[i+1]:
            return 'NO'
        i += 1

    return 'YES'



with open('input.txt') as inp, open('output.txt', 'w') as out:
    n, k = map(int, inp.readline().split())
    a = list(map(int, inp.readline().split()))

    out.write(determine_to_be_sorted(a, n, k))

