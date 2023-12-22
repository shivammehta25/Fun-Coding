import math
from functools import reduce

from helpers import read_file
from tqdm.auto import tqdm

# data = read_file("inputs/day6_test.txt")
data = read_file("inputs/day6.txt")




def A():
    def formatter():
        time = list(map(int, data[0].split(":")[1].strip().split()))
        record_distance = list(map(int, data[1].split(":")[1].strip().split()))

        return time, record_distance

    times, record_distances = formatter()
    total = []
    for i, t in enumerate(times):
        n_ways_to_win = 0
        for j in range(1, t):
            if j * (t - j) > record_distances[i]:
                # print(t, j, t - j)
                n_ways_to_win += 1
        total.append(n_ways_to_win)

    print(reduce(lambda x, y: x*y, total))



def B():    
    def formatter():
        time = int(data[0].split(":")[1].strip().replace(" ", ""))
        record_distance = int(data[1].split(":")[1].strip().replace(" ", ""))

        return time, record_distance

    time, record_distance = formatter()

    # f(h) = h * (T - h)
    # f(h) =>  h * T - h**2 > D
    # Solving using quadratic formula
    # h_1 = (T - sqrt(T**2 - 4D)) / 2
    # h_2 = (T + sqrt(T**2 - 4D)) / 2
    # Writing it in python
    
    h_1 = math.ceil((time - (time**2 - 4*record_distance)**0.5) / 2)
    # Either compute the second one
    h_2 = math.floor((time + (time**2 - 4*record_distance)**0.5) / 2)
    # Or compute the maximum of the f(h) function 
    # Derivative of f(h) is T - 2h = 0 => h = T/2
    print((time/2 - h_1)* 2 + 1) # include the center point
    print(h_2 - h_1 + 1)
    


if __name__ == "__main__":
    B()
