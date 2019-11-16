import math
from collections import Counter

def get_min_index(a):
    min_element = math.inf
    min_index = 0
    for i, v in enumerate(a):
        if v < min_element:
            min_element = v
            min_index = i

    return min_index, min_element


a = []
with open('input.txt') as inp:
    n = int(inp.readline())
    a = list(map(int,inp.readline().strip().split()))

    c = 0
    s = []
    for i, v in enumerate(a):
        i += 1
        if v != 0 or i == 1:
            c += 1
            s.append(1)
        else:
            m_i , element = get_min_index(s)
            s[m_i] += 1

    print(s)
o = open('output.txt', 'w')
c = Counter(s)
o.write(f'{len(s)}\n')
for k in c:
        o.write(f'{k} {c[k]}\n')

o.close()
    
