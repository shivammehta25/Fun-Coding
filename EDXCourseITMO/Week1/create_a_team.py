from math import sqrt


def distance(a, b, c):
    return sqrt(a**2 + b ** 2 + c**2)


def find_value(a, b, c):
    efficiency = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and k != i:
                    efficiency.append(distance(a[i], b[j], c[k]))
    return max(efficiency)


if __name__ == '__main__':
    with open('input.txt', 'r') as inp:
        a = list(map(int, inp.readline().split()))
        b = list(map(int, inp.readline().split()))
        c = list(map(int, inp.readline().split()))

    with open('output.txt', 'w') as out:
        out.write(str(find_value(a, b, c)))
        out.write('\n')
