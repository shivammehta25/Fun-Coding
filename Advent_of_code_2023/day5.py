import functools
import re

from helpers import read_file
from tqdm.auto import tqdm

# data = read_file("inputs/day5_test.txt")
# data = read_file("inputs/day5.txt")


class MappingList:
    def __init__(self):
        self.mappings = []
    
    def add(self, mapping):
        self.mappings.append(mapping)
    
    def __repr__(self):
        return "\n" + "\n".join([str(x) for x in self.mappings]) + "\n"
    
    def get_destination(self, number):
        mapped_number = -1
        for mapping in self.mappings:
            if mapping.source_start <= number < mapping.source_start + mapping.length:
                # print("Source: ", number)
                mapped_number = mapping.destination_start + (number - mapping.source_start)
                # print("Mapping: ", mapping)
                # print("Destination: ", mapped_number)
                break
        # if mapped_number == -1:
            # print("Source: ", number)
            # print("No Mapping:")
            # print("Destination: ", number)
        
        return number if mapped_number == -1 else mapped_number
    
    def sort(self):
        self.mappings.sort(key=lambda x: x.source_start)

class Mapping:
    def __init__(self, source_start, destination_start, length):
        self.source_start = int(source_start)
        self.destination_start = int(destination_start)
        self.length = int(length)
        
    def __repr__(self):
        return f"Map: {self.source_start} - {self.source_start + self.length} -> {self.destination_start} - {self.destination_start + self.length}"

global values

def formatter():
    seeds = list(map(int, data[0].strip().split(":")[1].strip().split(" ")))
    order = ["seed-to-soil", "soil-to-fetilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    ptr, i  = 0, 3
    global values
    values = {}
    
    new_list = MappingList() 
    while i < len(data):
        line = data[i].strip()
        if not line:
            i += 1
            continue
        if "map:" in line:    
            new_list.sort()
            values[order[ptr]] = new_list
            new_list = MappingList()
            ptr += 1
            i += 1
            continue
        
        destination, source, length = line.split(" ")
        new_list.add(Mapping(source, destination, length))
        i += 1 
    
    new_list.sort()
    values[order[ptr]] = new_list 

    return seeds, values


def A():
    seeds, values = formatter() 
    locations = [None for _ in range(len(seeds))]
    for i, seed in enumerate(seeds):
        number = seed
        for k, value in values.items():
            number = value.get_destination(number)
        locations[i] = number
        
    print(min(locations))
                
def B():
    seeds, values = formatter() 
    min_loc = float("inf")
    # print(seeds)
    for i in tqdm(range(0, len(seeds), 2)):
        for number in tqdm(range(seeds[i], seeds[i] + seeds[i + 1])):
            # number = 82
            number = get_mapped_number(number)
            min_loc = min(min_loc, number)
        
    print(min_loc)

@functools.lru_cache(maxsize=None)
def get_mapped_number(number):
    global values
    for k, value in values.items():
                # print(k)
        number = value.get_destination(number)
    return number


def BB():
    with open("inputs/day5.txt") as f:
        puzzle_input = f.readlines()
    
    puzzle_input = "".join(puzzle_input)
    
    # puzzle_input = "inputs/day5.txt"
    segments = puzzle_input.split('\n\n')
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))

    print(min_location)
    return min_location

if __name__ == "__main__":
    # A()
    BB()
        
        
        
            
        
        
            
        