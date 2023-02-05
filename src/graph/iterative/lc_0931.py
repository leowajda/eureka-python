from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        prev_row, n = matrix[0], len(matrix)

        for row in range(1, n):
            for col in range(0, n):
                left = float('inf') if col == 0 else prev_row[col - 1]
                upper = prev_row[col]
                right = float('inf') if col == n - 1 else prev_row[col + 1]

                matrix[row][col] += min(left, upper, right)
            prev_row = matrix[row]

        return min(prev_row)
