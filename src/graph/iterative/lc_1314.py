from typing import List


class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(matrix), len(matrix[0])
        block_sum = [[0 for _ in range(n)] for _ in range(m)]
        self.prefix_sum(matrix)

        for row in range(m):
            for col in range(n):
                a = matrix[row - 1 - k][col - 1 - k] if row - k > 0 and col - k > 0 else 0
                b = matrix[row - 1 - k][min(col + k, n - 1)] if row - k > 0 else 0
                c = matrix[min(m - 1, row + k)][col - 1 - k] if col - k > 0 else 0
                d = matrix[min(row + k, m - 1)][min(col + k, n - 1)]

                block_sum[row][col] = a - b - c + d

        return block_sum

    def prefix_sum(self, matrix: List[List[int]]) -> None:

        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            for col in range(n):
                a = matrix[row][col - 1] if col > 0 else 0
                b = matrix[row - 1][col] if row > 0 else 0
                c = matrix[row - 1][col - 1] if row > 0 and col > 0 else 0

                matrix[row][col] += a + b - c