from collections import defaultdict
from pprint import pprint

from helpers import read_file

# data = read_file("inputs/day3_test.txt")
data = read_file("inputs/day3.txt")

data = [[c for c in line.strip()] for line in data]



def assure_bounds(i, j):
    if 0 <= i < len(data) and 0 <= j < len(data[i]):
        return True
    return False

def B():

    def find_neighbouring_stars(row, s_ptr, e_ptr, debug=False):
        if debug:
            print("Row", row, s_ptr, e_ptr)
        for i in range(row-1, row+2):
            for j in range(s_ptr-1, e_ptr+2):
                if debug:
                    print(i, j)
                if (not assure_bounds(i, j)) or (i == row and s_ptr <= j <= e_ptr):
                    continue
                if debug:
                    print(data[i][j], i, j)
                if data[i][j] == "*":
                    return True, i, j 
        
        return False, None, None

    star_db = defaultdict(list)
    for i in range(len(data)): # 0
        j = 0
        s_ptr, e_ptr = None, None # 0
        
        while j < len(data[i]):
            if data[i][j].isdigit():
                if s_ptr is None:
                    s_ptr = j
                e_ptr = j
 
            else:
                if s_ptr is not None and e_ptr is not None:
                    neighbouring_star, star_i, star_j = find_neighbouring_stars(i, s_ptr, e_ptr)
                    if neighbouring_star:
                        star_db[(star_i, star_j)].append(int("".join(data[i][s_ptr:e_ptr + 1])))
                    else:
                        pass
                    s_ptr, e_ptr = None, None

            if j == len(data[i]) - 1:
                if s_ptr is not None and e_ptr is not None:
                    neighbouring_star, star_i, star_j = find_neighbouring_stars(i, s_ptr, e_ptr)
                    if neighbouring_star:
                        star_db[(star_i, star_j)].append(int("".join(data[i][s_ptr:e_ptr + 1])))
                    else:
                        pass
                    s_ptr, e_ptr = None, None
                    
                
            j += 1
                

    total = 0
    for k, v in star_db.items():
        if len(v) == 2:
            total += v[0] * v[1]
    
    print(total)
    
def A():

    def find_neighbouring_symbols(row, s_ptr, e_ptr, debug=False):
        if debug:
            print("Row", row, s_ptr, e_ptr)
        for i in range(row-1, row+2):
            for j in range(s_ptr-1, e_ptr+2):
                if debug:
                    print(i, j)
                if (not assure_bounds(i, j)) or (i == row and s_ptr <= j <= e_ptr):
                    continue
                if debug:
                    print(data[i][j], i, j)
                if data[i][j] != "." or data[i][j].isdigit():
                    return True
        
        return False


    total = 0
    for i in range(len(data)): # 0
        j = 0
        s_ptr, e_ptr = None, None # 0
        while j < len(data[i]):
            if data[i][j].isdigit():
                if s_ptr is None:
                    s_ptr = j
                e_ptr = j
 
            else:
                if s_ptr is not None and e_ptr is not None:
                    if find_neighbouring_symbols(i, s_ptr, e_ptr):
                        total += int("".join(data[i][s_ptr:e_ptr + 1]))
                    else:
                        pass
                    s_ptr, e_ptr = None, None

            if j == len(data[i]) - 1:
                if s_ptr is not None and e_ptr is not None:
                    if find_neighbouring_symbols(i, s_ptr, e_ptr):
                        total += int("".join(data[i][s_ptr:e_ptr + 1]))
                    else:
                        pass
                    s_ptr, e_ptr = None, None
                    
                
            j += 1
                
    print(total)
                        

if __name__ == "__main__":
    # A()
    B()
