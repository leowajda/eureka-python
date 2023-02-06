from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        prev_row, n = triangle[-1], len(triangle)

        for row in range(n - 2, -1, -1):
            m = len(prev_row)
            for col in range(m - 1):
                left, lower = prev_row[col + 1], prev_row[col]
                triangle[row][col] += min(left, lower)

            prev_row = triangle[row]

        return triangle[0][0]
