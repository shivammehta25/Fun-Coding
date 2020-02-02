# https://leetcode.com/problems/break-a-palindrome/
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        new_string = []

        replaced = 0

        for i, c in enumerate(palindrome):
            if c != 'a' and not replaced:
                c = 'a'
                replaced = i + 1
            new_string.append(c)

        if len(new_string) & 1 and (replaced - 1) == len(new_string) // 2:
            return palindrome[:-1] + 'b'

        if not replaced:
            new_string[-1] = 'b'

        return ''.join(new_string)


# Another good solution inspired by Errichto's solution
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        new_string = []
        for i, c in enumerate(palindrome):
            b = len(palindrome) - 1 - i
            if palindrome[i] == palindrome[b] and palindrome[i] != 'a':
                if b == i:
                    new_string.append(c)
                    continue

                return palindrome[:i] + 'a' + palindrome[i+1:]

            new_string.append(c)
        new_string[-1] = 'b'
        return ''.join(new_string)
