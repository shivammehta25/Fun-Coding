# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        using = {} # { c, d } # Space Constant (26) = O(1) 
        used = {} # {a,b} # Space Constant (26) = O(1)
        # abacabad
        #        ^
        for index, i in enumerate(s): # O(n)
            if i in using:
                used[i] = using[i]
                del using[i]
            elif i in used:
                continue
            else:
                using[i] = index

        if len(using):
            for i in using:
                return using[i]

        return -1
