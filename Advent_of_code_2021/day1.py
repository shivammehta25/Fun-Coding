# Have to count number of times the current number is greater than the previous one

from os import name


def open_file(file):
    with open(file) as f:
        data = [int(x.strip()) for x in f.readlines()]
    return data


def puzzle_a(data):
    x = 0
    for i in range(1, len(data)):
        x += 1 if (data[i] - data[i - 1] > 0) else 0

    print(x)


def puzzle_b(data):
    x = 0

    def convolution(i): return sum(data[i-2:i+1])

    for i in range(3, len(data)):
        x += 1 if convolution(i) > convolution(i - 1) else 0

    print(x)


if __name__ == '__main__':
    data = open_file("inputs/day1.txt")
    # puzzle_a(data)
    puzzle_b(data)
