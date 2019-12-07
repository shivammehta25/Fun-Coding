# https://app.codesignal.com/interview-practice/task/cHYqbQ9DiWmejAdeG/solutions
def composeRanges(nums):
    ans = []
    n = len(nums)
    if n <= 1:
        return [str(i) for i in nums]
    start = 0
    for i in range(n - 1):
        if nums[i] + 1 != nums[i + 1]:
            if start == i:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start])+ '->' + str(nums[i]) )

            start = i + 1

    if start == n - 1:
        ans.append(str(nums[start]))
    else:
        ans.append(str(nums[start]) + '->' + str(nums[n - 1]))
    
    return ans

