from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        state = [0, float('-inf'), float('-inf')]
        for price in prices:
            cooldown, acquisition, profit = state
            state = [max(profit, cooldown), max(acquisition, cooldown - price, profit - price), acquisition + price - fee]

        max_cooldown, _, max_profit = state
        return max(max_cooldown, max_profit)
