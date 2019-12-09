# https://app.codesignal.com/interview-practice/task/XBWN6DYRqPrKdMZs8/solutions
def houseRobber(nums): 
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    # 1 7 11 18
    for i in range(2,n): # 0
        nums[i] = nums[i] + max(nums[i - 2] , nums[i-3] if i-3 >= 0 else 0 )
    
    return max(nums[n-1], nums[n-2])
