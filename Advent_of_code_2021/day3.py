import numpy as np


def open_file(file):
    with open(file) as f:
        data = [x.strip() for x in f.readlines()]
    return data


def get_gama_eps_in_str(data):
    gamma = ''
    eps = ''

    for i in range(len(data[0])):
        bit_value = 0
        for j in range(len(data)):
            bit_value += int(data[j][i])

        max_occurance_bit = bit_value // (len(data) // 2)
        gamma += str(max_occurance_bit)
        eps += str(1 - max_occurance_bit)

    return gamma, eps


def day3_a(data):

    gamma, eps = get_gama_eps_in_str(data)

    gamma = int(gamma, 2)
    eps = int(eps, 2)

    print(gamma * eps)


def bit_criteria_1(rows, i):
    value = sum([int(x[i]) for x in rows]) / len(rows)
    return '0' if value < 0.5 else '1'


def bit_criteria_2(rows, i):
    value = sum([int(x[i]) for x in rows]) / len(rows)
    return '1' if value < 0.5 else '0'


def look_for_values(data, filtering_crit):

    filtered_data = data
    for i in range(len(data[0])):
        gamma_eps = filtering_crit(filtered_data, i)
        filtered_data = [x for x in filtered_data if x[i] == gamma_eps]
        if len(filtered_data) == 1:
            break

    return filtered_data[0]


def day3_b(data):

    o_rating = look_for_values(data, bit_criteria_1)
    co2_rating = look_for_values(data, bit_criteria_2)

    o_rating = int(o_rating, 2)
    co2_rating = int(co2_rating, 2)

    print(o_rating * co2_rating)


if __name__ == '__main__':
    data = open_file('inputs/day3.txt')

    # day3_a(data)
    day3_b(data)
