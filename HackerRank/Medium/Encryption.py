# https://www.hackerrank.com/challenges/encryption/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s, fptr):
    s.replace(' ', '')
    r_l = math.sqrt(len(s))
    l=len(s)
    rows = math.floor(r_l)
    columns = math.ceil(r_l)
    i, p = 0, 0
    while True:
        fptr.writelines(s[i])
        if i+ columns < l:
            i += columns
        else:
            if p == columns - 1:
                break
            fptr.writelines(' ')
            p += 1
            i = p
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s, fptr)


    fptr.close()
