# https://leetcode.com/problems/coin-change/submissions/
from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        output = [inf] * (amount + 1)
        output[0] = 0
        for value in range(1, amount + 1):
            for coin in coins:
                if value >= coin:
                    output[value] = min(output[value], output[value - coin] + 1)

        return output[-1] if output[-1] != inf else -1
