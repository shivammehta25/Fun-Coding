#!/usr/bin/env python3
class Solution:
    def firstMissingPositive(self, arr):
        if not arr:
            return 1
        m = max(arr)
        if m < 0:
            return 1
        cache = [0 for _ in range(m + 2)]
        for a in arr:
            if a >= 0:
                cache[a] = 1
        for i, v in enumerate(cache):
            if i == 0:
                continue
            if v == 0:
                return i

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.firstMissingPositive(arr))
