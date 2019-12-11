# https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1440/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)

    def reverse(self, s, i, j):
        if i < j:  # Base Case
            s[i], s[j] = s[j], s[i]
            self.reverse(s, i+1, j-1)  # Recursion Call
