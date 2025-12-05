from utils import Input
from bisect import bisect_right

day = 5


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = current
        
        if curr_start <= prev_end:
            # overlap merge
            merged[-1] = (prev_start, max(prev_end, curr_end))
        else:
            # No overlap new interval
            merged.append(current)
    
    return merged


def A():
    input = Input(day, 'a')
    
    INPUT = input.data

    
    intervals = []

    for i, line in enumerate(INPUT):
        if line.strip() == '':
            break
        
        s, e = map(int, line.split('-'))
        intervals.append((s,e))

    intervals = merge_intervals(intervals)

    ans = 0
    for j in range(i + 1, len(INPUT)):
        val = int(INPUT[j])
        idx = bisect_right(intervals, val,  key=lambda x: x[0]) - 1
        s, e = intervals[idx]
        if idx >= 0 and s <= val <= e:
            ans += 1
    
    print(ans)

        
def B():
    input = Input(day, 'a')
    INPUT = input.data
    
    intervals = []

    for i, line in enumerate(INPUT):
        if line.strip() == '':
            break
        
        s, e = map(int, line.split('-'))
        intervals.append((s,e))

    intervals = merge_intervals(intervals)

    ans = 0
    for s, e in intervals:
        ans += e - s + 1

    print(ans)
    

if __name__ == '__main__':
    A()
    print("-" * 50)
    B()
