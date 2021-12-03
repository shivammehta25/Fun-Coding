# Have to count number of times the current number is greater than the previous one

def open_file(file):
    with open(file) as f:
        data = [int(x.strip()) for x in f.readlines()]
    return data


# def puzzle_a(data):
#     x = 0
#     for i in range(1, len(data)):
#         x += 1 if (data[i] - data[i - 1] > 0) else 0

#     print(x)


def puzzle(data, window_size):
    x = 0

    def convolution(i):
        return sum(data[i - window_size + 1:i + 1])

    for i in range(window_size, len(data)):
        x += 1 if convolution(i) > convolution(i - 1) else 0
    print(x)


if __name__ == '__main__':
    data = open_file("inputs/day1.txt")
    # puzzle_a(data)
    puzzle(data, 1)
    puzzle(data, 3)
