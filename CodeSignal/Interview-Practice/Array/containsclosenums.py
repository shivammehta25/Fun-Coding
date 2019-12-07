# https://app.codesignal.com/interview-practice/task/njfXsvjRthFKmMwLC/solutions
def containsCloseNums(nums, k):
    info = {}
    for i, v in enumerate(nums):
        if v in info:
            if i - info[v] <= k:
                return True
        info[v] = i

    return False
