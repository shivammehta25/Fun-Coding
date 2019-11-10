
MAXTIME = 18000

with open('input.txt') as inp:
    n = int(inp.readline())
    problem_time = list(map(int, inp.readline().split()))
    problem_time = sorted(problem_time)
    current_time = 0
    max_n = 0
    for time in problem_time:
        if current_time + time > MAXTIME:
            break
        current_time += time
        max_n += 1

with open('output.txt', 'w') as o:
    o.write(str(max_n))
    o.write('\n')
