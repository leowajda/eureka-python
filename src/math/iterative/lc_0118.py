from typing import List


class Solution:
    def generate(self, n: int) -> List[List[int]]:

        rows = [[1]] + [[0] * (i + 1) for i in range(1, n)]
        prev_row = rows[0]

        for i in range(1, n):
            next_row = rows[i]
            next_row[0] = next_row[-1] = 1
            for j in range(1, i):
                next_row[j] = prev_row[j - 1] + prev_row[j]
            prev_row = next_row

        return rows
