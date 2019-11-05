# https://www.hackerrank.com/challenges/palindrome-index/problem?h_r=next-challenge&h_v=legacy
# Complete the palindromeIndex function below.
def palindromeIndex(s):
    n = len(s)
    i = 0
    while (i < n//2):
        if s[i] != s[n-1 - i]:
            if s[i] == s[n-2 - i] and s[i+1] == s[n-3 - i]:
                return n-i-1
            else:
                return i
        i += 1
    return -1


if __name__ == '__main__':
    assert palindromeIndex('aaab') == 3
    assert palindromeIndex('baa') == 0
    assert palindromeIndex('aaa') == -1
    print('Tests Passed')
