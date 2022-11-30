from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown, acquisition, profit = 0, float('-inf'), float('-inf')

        for price in prices:
            cooldown, acquisition, profit = max(profit, cooldown), max(cooldown - price, profit - price, acquisition), acquisition + price

        return max(cooldown, profit)
