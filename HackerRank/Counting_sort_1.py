# https://www.hackerrank.com/challenges/countingsort1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(n, arr):
    counter_array = [0] * (100)
    for i in range(n):
        counter_array[arr[i] ] += 1
    return counter_array
    
    # final_output = []
    # for i, v in enumerate(counter_array):
    #     for _ in range(v):
    #         final_output.append(i)
    # return final_output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(n, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
