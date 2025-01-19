from copy import deepcopy


def isincreasing(arr):
    return all([x > y and x - y <= 3 for x, y in zip(arr[1:], arr[:-1])])

def isdecreasing(arr):
    return all([x < y and y - x <= 3 for x, y in zip(arr[1:], arr[:-1])])


def B(inp):
    total = 0
    
    for line in inp:
        inp_arr = list(map(int, line.split()))
        found = False
        
        if isincreasing(inp_arr) or isdecreasing(inp_arr):
            total += 1
            continue
        
        for idx in range(len(inp_arr)):
            
            new_arr = [x for i, x in enumerate(inp_arr) if i != idx]
            print(new_arr, total)
            
            inc = isincreasing(new_arr)
            dec = isdecreasing(new_arr)
            print(inc, dec)

            if inc or dec:
                total += 1
                found = True
                break
                
        print()
        

    
    print(total)
        
        



def A(inp):
    total = 0
    for line in inp:
        arr = list(map(int, line.split()))
        n = len(arr)
        increasing = arr[0] < arr[1]
        add = True
        for i in range(1, n):
            if increasing and (arr[i] > (arr[i-1] + 3) or arr[i] <= arr[i - 1]):
                add = False 
            elif not increasing and (arr[i] < (arr[i-1] - 3) or arr[i] >= arr[i-1]):
                add = False
            
        if add:
            total += 1
        print(line, add)
    
    print(total)


if __name__ == "__main__":
    inp = None
    with open("inp.txt") as f:
        inp = f.readlines()
    B_o_n_solution(inp)