class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        paths = [1 for _ in range(n)]

        for _ in range(1, m):
            prev = 1
            for col in range(1, n):
                prev = paths[col] = paths[col] + prev

        return paths[-1]
