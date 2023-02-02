from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prev_state = [float('inf'), 0]
        for price in prices:
            prev_stock, prev_profit = prev_state
            prev_state = [min(prev_stock, price), max(prev_profit, price - prev_stock)]

        _, max_profit = prev_state
        return max_profit
