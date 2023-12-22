import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import cycle
from pprint import pprint

from helpers import read_file
from tqdm.auto import tqdm

# data = read_file("inputs/day9_test.txt")
data = read_file("inputs/day9.txt")


def formatter():
    values = []
    for line in data:
        values.append(list(map(int,line.strip().split())))

    return values

def shift_subtract(row):
    row_shifted = row[1:]
    return [x-y for x,y in zip(row_shifted, row)]


def A():
    rows = formatter()
    total = 0
    for row in rows:
        all_rows = [row]
        while True:
            row = shift_subtract(row)
            all_rows.append(row)
            if all(x == 0 for x in row):
                break

        
        for i in range(len(all_rows)- 1):
            last_element = all_rows[len(all_rows)-i-1][-1]
            next_element = last_element + all_rows[len(all_rows)-i-2][-1]
            all_rows[len(all_rows)-i-2].append(next_element) 
            # print(all_rows)
            # print()
        total += next_element
    
    print(total)
            
            
            
def B():
    rows = formatter()
    total = 0
    for row in rows:
        all_rows = [row]
        while True:
            row = shift_subtract(row)
            all_rows.append(row)
            if all(x == 0 for x in row):
                break

        
        current_element = 0 
        for i in range(1, len(all_rows)):
            last_row_index = len(all_rows)-i-1
            current_element = all_rows[last_row_index][0] - current_element
        
        print(current_element)
        total += current_element
    
    print(total)               





if __name__ == "__main__":
    # A()
    B()