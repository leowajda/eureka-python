from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock, profit = float('inf'), 0

        for price in prices:
            min_stock, profit = min(price, min_stock), max(price - min_stock, profit)

        return profit
