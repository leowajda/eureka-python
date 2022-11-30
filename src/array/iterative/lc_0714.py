from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cooldown, acquisition, profit = 0, float('-inf'), float('-inf')

        for price in prices:
            cooldown, acquisition, profit = max(profit, cooldown), max(cooldown - price, profit - price, acquisition), acquisition + price - fee

        return max(cooldown, profit)
