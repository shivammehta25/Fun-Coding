from re import I
from utils import Input
from functools import reduce

day = 6

def A():
    input = Input(day, 'a')
    INPUT = input.data
    INPUT = [x.split() for x in INPUT]
    ans = 0
    for j in range(len(INPUT[0])):
        operator = INPUT[-1][j]
        if operator == '+':
            ans += sum([int(x[j]) for x in INPUT[:-1]])
        elif operator == "*":
            ans += reduce(lambda x, y: x * y, [int(x[j]) for x in INPUT[:-1]])
        else:
            raise ValueError(f"Invalid operator {operator}")
    
    print(ans)


def get_numbers_by_operations(grid: list[str]) -> list[list[int]]:
    nums = []
    operation_vals = []
    for j in range(len(grid[0])):
        curr_num = ""
        for row in grid:
            if row[j].isdigit():
                curr_num += row[j]

        
        if curr_num == "": 
            # If still empty that means its a gap
            nums.append(operation_vals)
            operation_vals = []
        else:
            operation_vals.append(int(curr_num))
    
    nums.append(operation_vals)
    return nums
        

            


def B():

    input = Input(day, 'a')
    
    INPUT = input.data

    nums = get_numbers_by_operations(INPUT[:-1])
    operators = INPUT[-1].split()

    ans = 0
    for i, operator in enumerate(operators):
        if operator == '+':
            ans += sum(nums[i])
        elif operator == "*":
            ans += reduce(lambda x, y: x * y, nums[i])
        else:
            raise ValueError(f"Invalid operator {operator}") 

    print(ans)


    

if __name__ == '__main__':
    A()
    print("-" * 50)
    B()
