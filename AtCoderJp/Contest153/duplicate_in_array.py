def findDuplicate(nums):
    count = 0
    for _, num in enumerate(nums):
        if (count >> num) & 1 == 1:
            return num
        print(count >> num, count, num)
        count |= (1 << num)
    return -1


nums = list(map(int, input().split()))
print(findDuplicate(nums))
