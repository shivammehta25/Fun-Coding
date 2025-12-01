from collections import defaultdict, deque
from pprint import pprint

def load_file(path="dummy_inp.txt"):
    with open(path) as f:
        arr = f.readlines()
    
    rules = []
    pg_nums = []
    for i in range(len(arr)):
        line = arr[i].strip()
        if line.strip():
            rules.append(line.split("|"))
        else:
            break
    
    for i in range(i + 1, len(arr)):
        line = arr[i].strip().split(",")
        pg_nums.append(line)    
    return rules, pg_nums

def is_prev(prev_order, pg_num):
    # print(pg_num)
    for i in range(1, len(pg_num)):
        for j in range(i):
            if pg_num[i] not in prev_order:
                return False
            if pg_num[j] not in prev_order[pg_num[i]]:
                return False
    
    return True
        

def A(rules, pg_nums):
    prev_order = defaultdict(set)
    for a, b in rules:
        prev_order[b].add(a)

    prev_order = dict(prev_order)
    ans = []
    
    
    for pg_num in pg_nums:
        ok = True
        if is_prev(prev_order, pg_num):
            ans.append(pg_num)            
            
    s = 0
    for a in ans:
        l = len(a)
        if l & 1 == 0:
            s += int(a[l//2 - 1])
        else:
            s += int(a[l//2])
    
    print(s)
    return prev_order
    
    
def is_correct(ordered_dict, pg_num):
    prev_idx = -1
    for a in pg_num:
        idx = ordered_dict[a]
        if idx < prev_idx:
            return False
        prev_idx = idx
    
    return True

def fix_it(prev_rules, pg_num):
    n = len(pg_num)
    ans = [0] * n
    for i in range(n):
        current_element = pg_num[i]
        counter = 0
        if current_element not in prev_rules:
            ans[counter] = current_element
            continue

        for j in range(n):
            if i == j:
                continue
            checking_element = pg_num[j]
            if checking_element in prev_rules[current_element]:
                counter += 1
        ans[counter] = current_element
    
    return ans
                
        


def B(rules, pg_nums):
    prev_order = defaultdict(set)
    for a, b in rules:
        prev_order[b].add(a)

    prev_order = dict(prev_order)
    
    print(prev_order)
    ans = []    
    for pg_num in pg_nums:
        ok = True
        if not is_prev(prev_order, pg_num):
            pg_num = fix_it(prev_order, pg_num)
            ans.append(pg_num)
           
    s = 0
    for a in ans:
        l = len(a)
        if l & 1 == 0:
            s += int(a[l//2 - 1])
        else:
            s += int(a[l//2])
    
    print(s) 
     

if __name__ == "__main__":
    rules, pg_nums = load_file("inp.txt")
    # a1 = A(rules, pg_nums)
    # a2 = A_2(rules, pg_nums)    
    B(rules, pg_nums)