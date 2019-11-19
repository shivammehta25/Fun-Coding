from collections import defaultdict
from math import sqrt
count_d = defaultdict(int)
n = int(input())
a = []
for _ in range(n-2):
    line = list(map(int, input().split()))
    a.append(line)
    for e in line:
        count_d[e] += 1

data_array = []
for e in count_d:
    data_array.append((e, count_d[e]))

data_array = sorted(data_array, key=lambda x: x[1])
# print(f'data_array: {data_array}')
print(data_array)
data = [0] * (n)
max_element = data_array[-1][0]
last = n - 1 
first = 0
i = 0
while i < len(data_array):
    element = data_array[i]
    if i%2 == 0:
        data[first] = element[0]
        first += 1
        if element[0] == max_element:
            its_count = int(sqrt(element[1]))
            for j in range(0, its_count-1):
                data[first] = max_element
                first += 1
            i += j
        
    else:
        data[last] = element[0]
        last -= 1
        if element[0] == max_element:
            its_count = int(sqrt(element[1]))
            for j in range(0, its_count-1):
                data[last] = max_element
                last -= 1
            i += j
    

    i += 1

for line in a:
    if line[0] == max_element:
        q1, q2, q3 = line

# print(f'data: {data}')

for i, v in enumerate(data):
    if q1 == v:
        if data[i+1] == q2:
            if data[i+2] == q3:
                break
            else:
                swap_i = data.index(q3)
                temp = data[swap_i]
                data[swap_i] = data[i+2]
                data[i+2] = temp
        else:
            swap_i = data.index(q2)
            temp = data[swap_i]
            data[swap_i] = data[i+1]
            data[i+1] = temp



print(' '.join(map(str, data)))





