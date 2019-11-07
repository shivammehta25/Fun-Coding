#!/usr/bin/env python3
# https://codeforces.com/contest/4/problem/B

def get_values(time, sumtime):
    studied_hours = []

    total_min_time, total_max_time = 0, 0
    for i in range(len(time)):
        total_min_time += time[i][0]
        total_max_time += time[i][1]
    
    if total_min_time <= sumtime and sumtime <= total_max_time:
        for i, line in enumerate(time):
            print(i, studied_hours)
            min_time = line[0]
            max_time = line[1]
            if sumtime <= max_time and sumtime >= min_time:
                studied_hours.append(str(sumtime))
                sumtime -= max_time
                break
            elif sumtime < min_time:
                print('NO')
                exit(0)
            else:
                sumtime -= max_time
                studied_hours.append(str(max_time))

        if sumtime <= 0:
            print('YES')
            print(' '.join(studied_hours), end=' ')
            if len(studied_hours) < len(time):
                print(' '.join(['0'] * (len(time) - len(studied_hours))))
        else:
            print('NO')

    else:
        print('NO')


if __name__ == '__main__':
    d, sumtime = map(int, input().split())
    time = []
    for _ in range(d):
        time.append(list(map(int, input().split())))
    get_values(time, sumtime)
