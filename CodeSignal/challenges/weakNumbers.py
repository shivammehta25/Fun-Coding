# My Submission to this problem
# https://app.codesignal.com/challenge/wrD8sMDwk28cKQYJr
def weakNumbers(n):
    # Prime Sieve to compute number of divisors
    divisors = [1] * (n + 1)
    divisors[0] = 0
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            divisors[j] += 1
    # Compute Weakness:
    # Keep is current_maximum and its current_maximum count
    current_max = -1
    count = 0
    weakness = [0] * (n + 1)
    for i in range(1, len(divisors)):
        for j in range(1, i):
            if divisors[i] < divisors[j]:
                weakness[i] += 1
        if current_max < weakness[i]:
            current_max = weakness[i]
            count = 1
        elif current_max == weakness[i]:
            count += 1
    
    return [current_max, count]
    
