from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prev_state = [0, float('-inf'), float('-inf')]
        for price in prices:
            prev_cooldown, prev_acquisition, prev_profit = prev_state
            prev_state = [max(prev_profit, prev_cooldown), max(prev_acquisition, prev_cooldown - price), prev_acquisition + price]

        max_cooldown, _, max_profit = prev_state
        return max(max_cooldown, max_profit)
