import math


def get_optimum_value(n, t, p):
    min_en = math.inf
    min_en_index = 0
    o = []
    t_flag, p_flag = False, False
    for i in range(n):
        if t[i] > p[i]:
            o.append(t[i])
            t_flag = True
        else:
            o.append(p[i])
            p_flag = True

        enth = abs(t[i] - p[i])
        if min_en > enth:
            min_en_index = i
            min_en = enth

    if not t_flag:
        o[min_en_index] = t[min_en_index]
    if not p_flag:
        o[min_en_index] = p[min_en_index]

    return sum(o)


if __name__ == '__main__':
    with open('input.txt', 'r') as inp:
        n = int(inp.readline())
        p = list(map(int, inp.readline().split()))
        t = list(map(int, inp.readline().split()))

    with open('output.txt', 'w') as out:
        out.write(str(get_optimum_value(n, t, p)))
        out.write('\n')
