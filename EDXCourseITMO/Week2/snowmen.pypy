total_sum = 0
d = {0: {
    'sum': 0,
    'array': []}
}

with open('input.txt') as inp:
    n = int(inp.readline().strip())
    for i, line in enumerate(inp):
        i = i + 1
        t, m = map(int, line.strip().split())
        d[i] = {'sum': d[t]['sum'], 'array': [*d[t]['array']]}
        if m == 0:
            element = d[i]['array'].pop()
            d[i]['sum'] -= element
        else:
            d[i]['array'].append(m)
            d[i]['sum'] += m
        total_sum += d[i]['sum']
    print(d)
    print(total_sum)
        

with open('output.txt', 'w') as out:
    out.write(str(total_sum) + '\n')
