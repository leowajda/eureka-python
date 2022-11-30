from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown, acquisition, profit = 0, float('-inf'), float('-inf')

        for price in prices:
            cooldown, acquisition, profit = max(cooldown, profit), max(acquisition, cooldown - price), acquisition + price

        return max(profit, cooldown)
