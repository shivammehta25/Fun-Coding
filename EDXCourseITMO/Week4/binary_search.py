# You are given an array of  𝑛  elements in a non-decreasing order, and  𝑚  queries. Each query asks you to find where a certain element is located in the array above. You need to print the indices of the first and the last occurence of this element.

# Input
# The first line of the input file contains a single number  𝑛 , the size of the array  (1≤𝑛≤10^5) . The second line contains  𝑛  numbers in a non-decreasing order, which constitute the array. The third line contains a single number  𝑚 , the number of queries  (1≤𝑚≤10^5) . The fourth line contains  𝑚  numbers, which correspond to the queries. The array and the queries consist of integers which are non-negative and do not exceed  10^9 .

# Output
# For every query print a line consisting of the indices of the first and the last occurences of the corresponding number. If there is no such number in the array, output -1 -1.
# Example
# Input
# 5
# 1 1 2 2 2
# 3
# 1 2 3
# Output
# 1 2
# 3 5
# -1 -1


def bin_search(x, a):
    L = 0
    R = len(a) - 1
    while R >= L:
        mid = L + (R - L) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            R = mid - 1
        else:
            L = mid + 1
    return -1


def return_max_min(i, a):
    element = a[i]
    L = i
    R = i
    while L > 0:
        if a[L - 1] != element:
            break
        L -= 1

    while R < len(a) - 1:
        if a[R + 1] != element:
            break
        R += 1
    return L, R


with open('input.txt') as inp:
    n = int(inp.readline())
    a = list(map(int, inp.readline().split()))
    m = int(inp.readline())
    m = list(map(int, inp.readline().split()))

output_cache = {}
with open('output.txt', 'w') as out:
    for i in m:
        if i not in output_cache:
            index = bin_search(i, a)
            if index < 0:
                out.write('-1 -1\n')
                continue

            max_, min_ = return_max_min(index, a)
            out.write('{} {}\n'.format(max_+1, min_+1))
            output_cache[i] = (max_ + 1, min_ + 1)
        else:
            max_, min_ = output_cache[i]
            out.write('{} {}\n'.format(max_, min_))
