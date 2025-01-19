from collections import defaultdict
from copy import deepcopy


def get_psum(arr):
    psum = [0] * (len(arr) + 1)
    
    for i in range(1, len(psum)):
        psum[i] = psum[i-1] + arr[i - 1]
        
    return psum

def brute_force(arr):
    psum = get_psum(arr)
    print(psum)
    
    ans = {0}
    
    for i in range(1,len(psum)):
        for j in range(i):
            ans.add(psum[i] - psum[j])
    
    print(len(ans))
    print(" ".join(map(str, sorted(ans))))
    

def dfs_type_soln(arr):
    dp = defaultdict(int)
    
    N = len(arr)
    
    for i in range(N):
        curr_dp = deepcopy(dp)
        
            
    
        

def solve(arr):
    brute_force(arr)




if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        input()
        solve(list(map(int, input().split())))