from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prev_state = [float('-inf'), float('-inf'), 0]
        for price in prices:
            prev_sell, prev_acquisition, prev_profit = prev_state
            prev_state = [prev_acquisition + price, max(prev_acquisition, prev_profit - price, prev_sell - price), max(prev_profit, prev_sell)]

        max_sell, _, max_profit = prev_state
        return max(max_sell, max_profit)
