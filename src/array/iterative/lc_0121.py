from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        state = [float('inf'), 0]
        for price in prices:
            stock, profit = state
            state = [min(stock, price), max(profit, price - stock)]

        _, max_profit = state
        return max_profit
