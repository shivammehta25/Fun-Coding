from pprint import pprint
from tqdm.auto import tqdm

from itertools import combinations

log = False 
ansprint = print
if log:
    print = print
    pprint = pprint
else:
    print = lambda x: None
    pprint = print


def load_file(path="dummy_inp.txt"):
    with open(path) as f:
        arr = f.readlines()
     
    final = []
    for line in arr:
        value, numbers = line.strip().split(":")
        numbers = list(map(int, numbers.strip().split()))
        final.append((int(value), numbers))
        
    
    
    return final


# def is_valid(line):
#     value = line[0]
#     nums = line[1]
#     N = len(nums)
    
#     for n in range(1, N):
#         multiply_vals = combinations(nums[1:], n)
#         for multiply_val in multiply_vals:
#             values_computed = nums[0]
#             for i in range(1, len(nums)):
#                 if nums[i] in multiply_val:
#                     values_computed *= nums[i]
#                 else:
#                     values_computed += nums[i]
#             print(multiply_val, values_computed, value)
            
#             if values_computed == value:
#                 return True
    
    return False
            

def is_valid(value, numbers):
    if len(numbers) == 1:
        return value == numbers[0]

    first, second, others = numbers[0], numbers[1], numbers[2:]
    return is_valid(value, [first + second, *others]) or is_valid(value, [first * second, *others])
       

def is_valid_B(value, numbers):
    if len(numbers) == 1:
        return value == numbers[0]

    first, second, others = numbers[0], numbers[1], numbers[2:]
    return is_valid_B(value, [first + second, *others]) or is_valid_B(value, [first * second, *others]) or is_valid_B(value, [int(f"{first}{second}"), *others])
    

def A(inps):
    # pprint(inps)
    ans = 0
    for line in tqdm(inps):
        if is_valid(line[0], line[1]):
           ans += line[0]
           
    print(ans) 
    
def B(inps):
    # pprint(inps)
    ans = 0
    for line in tqdm(inps):
        print(line)
        print(is_valid_B(line[0], line[1]))       
        if is_valid_B(line[0], line[1]):
           ans += line[0]
           
    ansprint(ans) 

if __name__ == "__main__":
    arr = load_file("inp.txt")
    B(arr)

