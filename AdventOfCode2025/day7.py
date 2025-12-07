from utils import Input, print_2d
from collections import deque, defaultdict

day = 7 

def A():
    input = Input(day, 'a').convert_to_2d()
    
    INPUT = input.data


    M, N = len(INPUT), len(INPUT[0])
    s_i, s_j = 0, -1

    for i in range(N):
        if INPUT[0][i] == "S":
            s_j = i
            break
    
    queue = deque([(s_i, s_j)])

    ans = 0

    while queue:
        for _ in range(len(queue)):
            s_i, s_j = queue.popleft()
            if s_i + 1 >= M:
                continue
                
            if INPUT[s_i + 1][s_j] == ".":
                INPUT[s_i + 1][s_j] = '|'
                queue.append((s_i + 1, s_j))
            elif INPUT[s_i + 1][s_j] == "^":
                ans += 1
                if s_j - 1 >= 0:
                    INPUT[s_i + 1][s_j - 1] = '|'
                    queue.append((s_i + 1, s_j - 1))
                if s_j + 1 < N:
                    INPUT[s_i + 1][s_j + 1] = '|'
                    queue.append((s_i + 1, s_j + 1))

    # print_2d(INPUT)

    print(ans)



def B():

    val = Input(day, 'a').convert_to_2d(strip=True)
    INPUT = val.data


    M, N = len(INPUT), len(INPUT[0])

    grid = [[0] * N for _ in range(M)]
    s_i, s_j = 0, -1

    for i in range(N):
        if INPUT[0][i] == "S":
            s_j = i
            break
    
    grid[s_i][s_j] = 1

    for i in range(1, M):
        for j in range(N):
            if INPUT[i][j] == '^':
                if j - 1 >= 0:
                    grid[i][j - 1] += grid[i - 1][j]
                if j + 1 < M:
                    grid[i][j + 1] += grid[i - 1][j]
            else:
                grid[i][j] += grid[i-1][j]
        
    print(sum(grid[-1]))

    

if __name__ == '__main__':
    A()
    print("-" * 50)
    B()
