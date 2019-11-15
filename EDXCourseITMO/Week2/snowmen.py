total_sum = 0
with open('input.txt') as inp:
    n = int(inp.readline().strip())
    weights = [0] * (n + 1)
    prev = [0] * (n + 1)
    for i, line in enumerate(inp):
        i = i + 1
        t, m = map(int, line.strip().split())
        if m == 0:
            previous_element = prev[t]
            weights[i] = weights[previous_element]
            prev[i] = prev[previous_element]
        else:
            weights[i] = weights[t] + m
            prev[i] = t

        total_sum += weights[i]
    print(total_sum)


with open('output.txt', 'w') as out:
    out.write(str(total_sum) + '\n')
