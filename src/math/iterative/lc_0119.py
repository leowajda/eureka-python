from typing import List


class Solution:
    def getRow(self, n: int) -> List[int]:

        row = [1] + ([0] * n)

        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        return row