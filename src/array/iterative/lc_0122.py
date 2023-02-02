from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        state = [float('-inf'), float('-inf'), 0]
        for price in prices:
            sell, acquisition, profit = state
            state = [acquisition + price, max(acquisition, profit - price, sell - price), max(profit, sell)]

        max_sell, _, max_profit = state
        return max(max_sell, max_profit)
