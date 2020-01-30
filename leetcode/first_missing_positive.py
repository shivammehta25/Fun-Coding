#!/usr/bin/env python3
# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def segregate_positives(self, a):
        j = 0
        for i in range(len(a)):
            if a[i] <= 0:
                a[i], a[j] = a[j], a[i]
                j += 1
        return a[j:]
                
    
    def firstMissingPositive(self, arr):
        arr = self.segregate_positives(arr)
        for i in range(len(arr)):
            if (abs(arr[i]) - 1) < len(arr):
                arr[abs(arr[i]) - 1] = - abs(arr[abs(arr[i]) - 1])
        
        for i in range(len(arr)):
            if arr[i] > 0:
                return i + 1

        return len(arr) + 1


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.firstMissingPositive(arr))
