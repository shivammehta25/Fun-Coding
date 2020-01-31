class Solution:

    def firstMissingPositive(self, arr):
        arr = [a for a in sorted(set(arr)) if a > 0]
        for i in range(1, len(arr)+1):
           # print(arr[i-1], i)
            if arr[i] != i:
                return i
        return len(arr) + 1
            
                

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.firstMissingPositive(arr))
