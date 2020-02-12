# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        if k == 1:
            return arr

        Q = deque()
        answer = []
        for i in range(k):
            while Q and arr[Q[-1]] <= arr[i]:
                Q.pop()
            Q.append(i)

        
        for i in range(k, len(arr)):

            answer.append(arr[Q[0]])

            while Q and Q[0] <= i - k:
                Q.popleft()
            
            while Q and arr[Q[-1]] <= arr[i]:
                Q.pop()
            
            Q.append(i)
            
        if Q: answer.append(arr[Q[0]])

        return answer
        
