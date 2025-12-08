import enum
from utils import Input, print_2d
from collections import deque
import math

day = 8


def dist(x: tuple[int, int, int], y: tuple[int, int, int]) -> float:
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)


def A():
    input = Input(day, 'a').from_csv(to_int=True, strip=True)
    
    INPUT = input.data

    connected = set()

    dist_list = {}

    for i in range(len(INPUT)):
        num1 = tuple(INPUT[i])
        for j in range(i + 1, len(INPUT)):
            num2 = tuple(INPUT[j])
            if num1 != num2 and (num1, num2) not in dist_list and (num2, num1) not in dist_list:
                dist_list[tuple(sorted((num1, num2)))] = dist(num1, num2)
   
    dist_list = sorted(dist_list.items(), key=lambda x: x[1], reverse=True)

    circuits: list[set[tuple[int, int, int]]] = [ set([tuple(x)]) for x in INPUT ]

    def find_in_circuits(n: tuple[int, int, int], circuit: list[set[tuple[int, int, int]]]) -> int:
        n_i = -1
        for i, val in enumerate(circuit):
            if n in val:
                n_i = i
                break
        return n_i


    itr = 0
    while len(circuits) != 1:
        itr += 1
        (a, b), _ = dist_list.pop()
        
        a_i = find_in_circuits(a, circuits)
        b_i = find_in_circuits(b, circuits)

        if a_i == b_i:
            continue

        assert a_i >= 0
        assert b_i >= 0

        circuits[a_i] = circuits[a_i].union(circuits[b_i])
        circuits.pop(b_i)


        if itr == 1000:
            x, y, z = sorted([len(x) for x in circuits], reverse=True)[:3]
            print("Part A:", x * y * z)

            

def B():
    input = Input(day, 'a').from_csv(to_int=True, strip=True)
    
    INPUT = input.data

    connected = set()

    dist_list = {}
    
    for i in range(len(INPUT)):
        num1 = tuple(INPUT[i])
        for j in range(i + 1, len(INPUT)):
            num2 = tuple(INPUT[j])
            if num1 != num2 and (num1, num2) not in dist_list and (num2, num1) not in dist_list:
                dist_list[tuple(sorted((num1, num2)))] = dist(num1, num2)
    
    dist_list = sorted(dist_list.items(), key=lambda x: x[1], reverse=True)

    circuits: list[set[tuple[int, int, int]]] = [ set([tuple(x)]) for x in INPUT ]

    def find_in_circuits(n: tuple[int, int, int], circuit: list[set[tuple[int, int, int]]]) -> int:
        n_i = -1
        for i, val in enumerate(circuit):
            if n in val:
                n_i = i
                break
        return n_i


    itr = 0
    while len(circuits) != 1:
        itr += 1
        (a, b), _ = dist_list.pop()
        
        a_i = find_in_circuits(a, circuits)
        b_i = find_in_circuits(b, circuits)

        if a_i == b_i:
            continue

        assert a_i >= 0
        assert b_i >= 0

        circuits[a_i] = circuits[a_i].union(circuits[b_i])
        circuits.pop(b_i)


    if len(circuits) == 1:
            print("Part B", a[0] * b[0])

            



if __name__ == '__main__':
    A()
    print("-" * 50)
    B()
