# Naive Solution to this problem

def maxSubarray(inputArray):
    N = len(inputArray)
    max_sum = 0
    for i in range(N):
        for j in range(N-1, i, -1):
            max_sum = max(max_sum, sum([inputArray[i]] + inputArray[i+1:j]))
            
    return max_sum
