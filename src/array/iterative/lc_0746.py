from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        a, b = 0, cost[-1]
        for i in range(n - 2, -1, -1):
            a, b = b, min(a, b) + cost[i]

        return min(a, b)