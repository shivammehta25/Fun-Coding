# https://leetcode.com/problems/missing-number/submissions/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(abs(sum(nums) - ((n * (n + 1)) / 2)))
