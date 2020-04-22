t = int(input())

while t:
    t -= 1
    n = int(input())
    if n % 4 != 0:
        print("NO")
        continue

    print("YES")
    
    n //= 2

    s_even = n * (n + 1)

    s_odd_minus_one = (n - 1)**2

    last_odd_number = s_even - s_odd_minus_one

    print(' '.join([str(2*i) for i in range(1,n+1)]), end=" ")
    print(" ".join([str(2*i - 1) for i in range(1,n)]), end=" ")
    print(last_odd_number)
